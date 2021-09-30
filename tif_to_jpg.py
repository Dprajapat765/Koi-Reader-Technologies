#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:55:40 2021

@author: dinesh
"""
import os
from PIL import Image

# add path of all the files
img_PATH = "/home/dinesh/Desktop/pdf_to_img/all_dataset/main/images/namrata_maam/"
# store all file names in a list
pdf_file = [str(img_PATH+i) for i in os.listdir(img_PATH) if i.endswith(".TIF")]

index = 0
# loop to access every file
for img in pdf_file:
# open every file 
    im = Image.open(img)
    #save all files in folder called "jpg_files"
    im.save("/home/dinesh/Desktop/pdf_to_img/all_dataset/main/images/namrata_maam/" + str(img[int(len(img_PATH)):-4]) + str(index) + ".jpg")
    index+=1
   
