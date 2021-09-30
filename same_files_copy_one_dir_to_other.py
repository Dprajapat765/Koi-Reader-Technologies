import os 
from PIL import Image
import shutil
#img_PATH = "/home/dinesh/Desktop/pdf_to_img/all_dataset/images/"
path1 = "/home/dinesh/Desktop/pdf_to_img/each_word_annots/mukesh/all images with jason/"
path2 = "/home/dinesh/Desktop/pdf_to_img/each_word_annots/all/"

pdf_file = [str(path1+i) for i in os.listdir(path1) if i.endswith(".jpg")]
pdf_file2 = [str(path2+j) for j in os.listdir(path2) if j.endswith(".jpg")]
dest_dir = "/home/dinesh/Desktop/pdf_to_img/each_word_annots/mukesh/may_10/"
for file in pdf_file:
    if file not in pdf_file2:
        shutil.copy(file,dest_dir)

