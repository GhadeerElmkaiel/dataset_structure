import os
import numpy as np
from PIL import Image

path_to_orig = "/home/ghadeer/Projects/Datasets/SberMerged/test/images/"
path_to_flipped = "/home/ghadeer/Projects/Datasets/SberMerged/test/images_flipped/"
path_to_sem_orig = "/home/ghadeer/Projects/Datasets/SberMerged/test/Semantic/"
path_to_sem_flipped = "/home/ghadeer/Projects/Datasets/SberMerged/test/Semantic_flipped/"

images = [x for x in os.listdir(path_to_orig) if "." in x]
masks = [x for x in os.listdir(path_to_sem_orig) if "." in x]

for name in images:
    path = path_to_orig+name
    image = Image.open(path).convert('RGB')
    flipped_image = image.transpose(method = Image.FLIP_LEFT_RIGHT)
    flipped_image.save(path_to_flipped+name)

for name in masks:
    path = path_to_sem_orig+name
    image = Image.open(path).convert('RGB')
    flipped_image = image.transpose(method = Image.FLIP_LEFT_RIGHT)
    flipped_image.save(path_to_sem_flipped+name)