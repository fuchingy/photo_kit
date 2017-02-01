#!/bin/bash
# 1. Change directory to ./finish
# 2. Mount the centralized photo folder on NFS
# 3. Execute the following command
rsync -avz --progress -e ssh ./ /Volumes/photo/
