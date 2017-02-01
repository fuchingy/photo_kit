#!/usr/bin/python
import os, sys
import shutil
import re

reload(sys)
sys.setdefaultencoding('utf8')

# Convert the folder name exported from Photos into formated name
def get_format_name(folder_name):
    m1 = re.match(r"([0-9]+)[\xe5\xb9\xb4]+([0-9]+)[\xe6\x9c\x88]+([0-9]+)[\xe6\x97\xa5].", folder_name)
    m2 = re.match(r".*, ([0-9]+)[\xe5\xb9\xb4]+([0-9]+)[\xe6\x9c\x88]+([0-9]+)[\xe6\x97\xa5].", folder_name)
    if(m1):
        year = m1.group(1)
        month = m1.group(2)
        if(len(month)==1):
            month = '0' + month
        day = m1.group(3)
        if(len(day)==1):
            day = '0' + day
        format_name = year + month + day
    elif(m2):
        year = m2.group(1)
        month = m2.group(2)
        if(len(month)==1):
            month = '0' + month
        day = m2.group(3)
        if(len(day)==1):
            day = '0' + day
        format_name = year + month + day

    if( m1 or m2 ):
        return year, format_name
    else:
        return None, None

# Create a temporal folder
try:
    os.makedirs('.tmp')
except OSError:
    if not os.path.isdir('.tmp'):
        raise

# Search for all files and move them in the temporal folder
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        folder_name = os.path.split(root)[1]
        year, format_name = get_format_name(folder_name)
        if(format_name != None):
            dst = os.path.join('.tmp/', year, format_name)
            try:
                os.makedirs(dst)
                print('Create ' + dst)
            except OSError:
                if not os.path.isdir(dst):
                    raise
            # move file to format_name
            print("Move " + os.path.join(root, file)+ " to " + dst) 
            shutil.move(os.path.join(root, file), dst) 

# Delete all folders
dirs = os.listdir(os.getcwd())
for dir in dirs:
    year, format_name = get_format_name(dir)
    if(format_name != None):
        print("Remove " + dir)
        os.rmdir(os.path.join(os.getcwd(), dir))

# Rename the temporal folder
shutil.move('./.tmp', './finish')

