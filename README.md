 Photo Kit

  What is it?
  -----------

  The purpose is to struct and rename the photos exported by Apple Photos to have a
  consistent naming convention and well-organized folder structure. The results can
  be merged into a centralized folder via rsync, and that folder can be sync with
  cloud storage such as Amazon Drive for data backup.

  What's the problem?
  -------------------

  Although Apple Photos is nice to manage photos, its photo management methodology
  and source code are not public. This has two drawbacks. First, it forces users to
  use iCloud to share photos, since 3rd parties such as Google Photo does not know
  how to read the photos. Second, it limits the scalability, since as the photo
  number increases, the disk storage won't be able to store all photos in a single
  Photos library, especially in the case of SSD. Users will inevitablly keep old
  photos in separate Photos libraries else where, such as external HD or NAS.
  However, browsing photos in different libraries is very inconvenient: users need
  to close Photos before open another library.

  To solve the problem, the simplest solution is the old style folder-based
  management approach, such as below. Every 3rd party software understands this
  structure. Management is straight forward. Scalability is good.

  ./2015
    ./20150523
    ./20150922
  ./2016
    ./20160204
    ./20161022

  Although folder-based management is good, Apple Photos still has nice features
  that we wants to keep. My solution is to use Apple Photos to import photos in
  iDevice. When the size exceeds a threshold (e.g., 50GB), export photos in
  folder-based structure and rsync to a centralized storage in NAS. That
  centralized storage sync with Amazon Cloud Drive for backup.

  Such methodology is good, but has a minor issue: the Subfolder format exported
  by Apple Photos has Chinese characters (2016年12月3日), which is not good for
  storage and data process convenience. The purpose of this kit is to convert the
  folder name and structure into formated ones categorized by year, as the above
  example.

  Installation
  ------------

  No installation is required.
  However, python, bash, rsync are required.

  Usage
  -----

  Step 1: export photos using Apple Photos.

    1. Select photos you want to export.
    2. Click File > Export > Export Unmodified Original... to export photos to a
       folder, e.g., /export_photo

  Step 2: rename/restructure exported photos

    1. change directory into the exported folder

       $ cd /export_photo

    2. call script to rename/restructure

       $ ./rename_folder.py

       The results will be stored in /export_photo/finish 

  Step 3: rsync the structured results into a centralized folder

    1. One can reference rsync.sh to do this. 
    

  Licensing
  ---------

  Please see the file called LICENSE.

  Contacts
  --------

  Fu-Ching Yang <fcyangesl@gmail.com>
