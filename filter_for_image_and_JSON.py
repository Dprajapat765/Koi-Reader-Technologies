#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:10:33 2021

@author: dinesh
"""


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
ltr = []
rtl = []


def funct1(arr):
    count = -1
    for i in range(len(arr)):
        ltr.append(arr[i][i])
        rtl.append(arr[i][count])
        count -=1        
    diff = sum(rtl) - sum(ltr)
    return diff

funct1(arr)





import os
import shutil
import sys


path = "/home/dinesh/Downloads/temp/"

try:
    os.makedirs(str(path)+"images/")
    print("images folder created successfully.")
    os.makedirs(str(path)+"labels/")
    print("labels folder created successfully.")
except FileExistsError:
    print("images folder already exists!!!")
    print("labels folder already exists!!!")
    
images = os.listdir(path+"test/")

def create_labels_txt():
    labels_path = os.path.join(path+"labels/")
    with open(str(labels_path) + str(i.split("\t")[0][:-4]) + ".txt", "w") as label_txt:
        label_txt.write(str(i.split("\t")[1][:-2]))
    return "{} created".format(str(i.split("\t")[0][:-4]))

def move_images():
    images_path = os.path.join(path+"images/")
    return shutil.move(path+"test/" + str(i.split("\t")[0]), images_path+ str(i.split("\t")[0]))

with open(str(path)+"test.txt") as file:  
    data = file.readlines()
    for i in data:
        if i.split("\t")[0] in images:
            try:
                move_images()
                create_labels_txt()
            except FileNotFoundError:
                print("File not found")
                





