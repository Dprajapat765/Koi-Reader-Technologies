from pdf2image import convert_from_path
import json, os
from tqdm import tqdm

# enter the path where all pdf files stored
pdf_path = "/home/dinesh/Downloads/New Age/" 

# enter the path where all pdf files stored
output_dir_path = "/home/dinesh/Downloads/New Age/output"

#list comprehension to fetch path of all files
pdf_file = [str(pdf_path+i) for i in os.listdir(pdf_path) if i.endswith(".pdf") or i.endswith(".PDF")]

#print total number of files
print("total pdf files:",len(pdf_file))

# loop to iterate every file
for pdf in tqdm(pdf_file):
	# convert every file - 
    pil_images = convert_from_path(str(pdf_path), dpi=200)
	#loop to save every file
    for k, image in enumerate(pil_images):
        image.save(str(output_dir_path) +str(pdf[len(pdf_path):-4]) + str(k) + ".jpg")
        print("image saved", k)
		
		

