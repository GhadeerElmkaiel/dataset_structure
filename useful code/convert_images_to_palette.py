from PIL import Image
import numpy as np
import os

split = "validation"
path_to_masks = split+"/Semantic/"
path_to_edited = split+"/Semantic_palette/"
os.makedirs(path_to_edited, exist_ok=True)

src_palette = Image.open("all_palette.png")
src_palette = src_palette.convert("P", palette=Image.ADAPTIVE)

images = [x for x in os.listdir(path_to_masks) if "." in x]
for name in images:
    img = Image.open(path_to_masks+name).quantize(palette=src_palette)
    img.save(path_to_edited+name)