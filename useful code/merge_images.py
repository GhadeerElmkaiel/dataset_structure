
from PIL import Image 
import os
import re

path_to_images= "/home/ghadeer/Projects/Datasets/Outdoor/SELECTED/"
path_to_res= "/home/ghadeer/Projects/Trans2Seg/runs/visual/Trained_on_Sber2400_tested_on_Outdoor/Orig/"
#path_to_merged = "/home/ghadeer/Projects/Datasets/testing_result/"+re.split('[/]', path_to_res)[-2]
path_to_merged =  "/home/ghadeer/Projects/Trans2Seg/runs/visual/Trained_on_Sber2400_tested_on_Outdoor/Merged/"

os.makedirs(path_to_merged, exist_ok=True)

names = [name for name in os.listdir(path_to_images) if "." in name]

for name in names:
    n = re.split('[.]', name)
    img = Image.open(path_to_images+name)
    mask = Image.open(path_to_res+n[0]+".png")
    size = img.size
    new_img = Image.new('RGB', (size[0], size[1]*2))
    new_img.paste(img, (0, 0))
    new_img.paste(mask, (0, size[1]))
    new_img.save(os.path.join(path_to_merged, name[:-4]+".png"))

