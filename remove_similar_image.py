#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 18:29:06 2021

@author: dinesh
"""

import os
print("type 'help' for instructions of removing similar images")

# mention path of both directories
path1 = "/home/dinesh/Downloads/python_scripts/Refernce_images_18/RT_on_ground_Pallet/"  
path2 = "/home/dinesh/Downloads/python_scripts/Refernce_images_18/RT_on_ground_Pallet2/"
dir1 = os.listdir(path1)
dir2 = os.listdir(path2)
main_dir = list(set(dir1+dir2))

user = input('Remove from (write "dir1" or something else)>>')

if user == "HELP" or user == "help" or user == "Help":
    print("To remove similar images from first directory, type - 'dir1' ")
    print("To remove similar images from second directory, type - 'dir2 or anything on console' ")

else:
    for file in main_dir:
        if file in dir1 and file in dir2:
            if user=='dir1':
                os.remove(path1+file)
            else:
                os.remove(path2+file)