# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:05:00 2023

@author: Nicholas Flood
"""

from PIL import Image as img
import os
import numpy as np
import pandas as pd

path = "sketches_png/png/"
Animals = ['ant', 'bear (animal)', 'bee', 'butterfly', 'camel', 'cat', 'cow', 'crab', 'dog', 'dolphin', 'dragon', 'duck', 'elephant', 'fish', 'flying bird', 'frog', 'giraffe', 'hedgehog', 'horse', 'kangaroo', 'lion', 'lobster', 'mermaid', 'monkey', 'octopus', 'owl', 'panda', 'parrot', 'penguin', 'pig', 'pigeon', 'rabbit', 'santa claus', 'scorpion', 'sea turtle', 'seagull', 'shark', 'sheep', 'snail', 'snake', 'spider', 'sponge bob', 'squirrel', 'standing bird', 'swan', 'tiger', 'zebra']
animalPaths = []
for animal in Animals:
    animalPaths.append(os.path.join(path, animal))

finalData = []

# iterates through every label in categories
for animal in Animals:
    currentPath = os.path.join(path, animal)
    #iterates through every image in the labels
    for image in os.listdir(currentPath):
        currentImage = img.open(os.path.join((animalPaths[0]),(os.listdir(animalPaths[0])[0])))

        data = np.asarray(currentImage)
        data1D = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                data1D.append(data[i][j])
        currentImage.close
        data1D.append(animal)
        finalData.append(data1D)
        
    print("done with " + animal)
    
print("done")

dataXL = pd.DataFrame(finalData)
dataXL.to_excel("sketches_png/Categories/Animals/data.xlsx")


