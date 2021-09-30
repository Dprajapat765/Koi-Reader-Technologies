#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:29:21 2021

@author: dinesh
"""



from pdf2image import convert_from_path
import os

# enter the path where all pdf files stored
parent_folder = "/home/dinesh/Downloads/Checkbox/"

# enter the path where all pdf files stored
output_dir_path = "/home/dinesh/Documents/pdf_to_image/"


for (root,dirs,files) in os.walk(parent_folder):
    for file in files:
        if file.endswith('.pdf'):
            pil_images = convert_from_path(str(root+'/'+file))
            for k, image in enumerate(pil_images):
                if os.path.exists(str(output_dir_path)+ root.split('/')[-1]+'/' ):
                    image.save(str(output_dir_path)+ root.split('/')[-1]+'/'+str(file[:-3]) + str(k) + ".jpg")
                    print("image saved", k)
                else:
                    os.makedirs(str(output_dir_path)+root.split('/')[-1]+'/' )
                    image.save(str(output_dir_path)+ root.split('/')[-1]+'/' +str(file[:-3]) + str(k) + ".jpg")


