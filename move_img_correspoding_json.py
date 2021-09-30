#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:12:21 2021

@author: Dinesh
"""


import os
import shutil 

#path = "/home/jarvis/Downloads/DSD Systems - One-Touch Delivery System (Pepsi -- Geo Box)/"
path = "/home/jarvis/Downloads/DSD Systems - One-Touch Delivery System (Pepsi -- Geo Box)/"
dest_path = "/home/jarvis/Downloads/annots/"
files = os.listdir(path)

for i in files:
    for k in files:
        if i.endswith(".jpg"):
            if k.endswith(".json"):
                if i[:-4] == k[:-5]:
                    shutil.move(path+i,dest_path )
                    shutil.move(path+k,dest_path)