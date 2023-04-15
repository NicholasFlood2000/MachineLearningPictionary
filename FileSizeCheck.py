# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:24:08 2023

@author: Nicholas Flood
"""

from PIL import Image as img
import os

path = "sketches_png/png/"
suffix = ".png"
currentPath = path + "airplane/1" + suffix
image = img.open(currentPath)
size = image.size

folders = os.listdir(path)

for folder in os.listdir(path):
    currentPath = os.path.join(path, folder)
    for png in os.listdir(os.path.join(path, folder)):
        if(() and (not (img.open(os.path.join(currentPath, png)).size == size))):
            print("not same size")
print("done")
            