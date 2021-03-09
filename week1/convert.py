#!/usr/bin/env python3
from PIL import Image
import os


current_dir = os.getcwd()
source_dir = current_dir + '/images/'
tar_dir = "/opt/icons/"
#photo_list = os.listdir(source_dir)
#print(photo_list)

if not os.path.exists(tar_dir):
    os.makedirs(tar_dir)

for file in os.listdir(source_dir):
    if not file.startswith('.'):
        target = Image.open(source_dir + file)
        target.convert('RGB').rotate(270).resize((128,128)).save(tar_dir + file, "JPEG")
        target.close()
