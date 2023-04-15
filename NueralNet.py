# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:05:00 2023

@author: Nicholas Flood
"""

from PIL import Image as img
import os
import numpy as np
import pandas as pd
import math
import torch
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense

path = "sketches_png/Categories"
category = "Space"

categoryPath = (os.path.join(path, category))
categoryPathImages = os.path.join(categoryPath, "Images")

class Image():
    def __init__(self):
        bytes = []
        label = ""

def CNN(dataPath):
    image_height = 900
    image_width  = 900
    batches = 32
    
    train_ds = tf.keras.utils.image_dataset_from_directory(dataPath, 
           labels="inferred", label_mode="categorical", color_mode="grayscale",
           seed=123, image_size=(image_height, image_width), batch_size=batches,
           validation_split=0.1, subset="training")
    test_ds = tf.keras.utils.image_dataset_from_directory(dataPath, 
           labels="inferred", label_mode="categorical", color_mode="grayscale",
           seed=123, image_size=(image_height, image_width), batch_size=batches,
           validation_split=0.1, subset="validation")

    #defining model
    model=Sequential()
    #normalization layer
    model.add(tf.keras.layers.Rescaling(1./255))
    #adding convolution layer
    model.add(Conv2D(32,(3,3),activation='relu',input_shape=(900,900,1)))
    #adding pooling layer
    model.add(MaxPool2D(3,3))
    #adding fully connected layer
    model.add(Flatten())
    model.add(Dense(100,activation='relu'))
    #adding output layer
    model.add(Dense(3,activation='softmax'))
    #compiling the model
    #sparse_categorical_crossentropy
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    return model, train_ds, test_ds

def train(model, categoryPath, categoryPathImages):
    model, train_ds, test_ds = CNN(categoryPathImages)
    model.fit(train_ds, validation_data=test_ds, epochs=2)
    model.save(categoryPath)
    
    
finalModel = CNN(categoryPathImages)
train(finalModel, categoryPath, categoryPathImages)
print("done")