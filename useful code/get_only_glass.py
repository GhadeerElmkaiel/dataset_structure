import os
import numpy as np
from PIL import Image

path_to_masks = "Glass/"

img_names = [img_name for img_name in os.listdir(path_to_masks)]

only_glass = []
for name in img_names:
    mirror_mask = Image.open("Mirror/"+name)
    mirror_mask = mirror_mask.convert("L")
    mirror_arr = np.array(mirror_mask, dtype="?")

    other_mask = Image.open("Other optical surface/"+name)
    other_mask = other_mask.convert("L")
    other_arr = np.array(other_mask, dtype="?")
    x = sum(sum(other_arr))
    y = sum(sum(mirror_arr))
    if x==0 and y==0:
        only_glass.append(name)

print(only_glass)