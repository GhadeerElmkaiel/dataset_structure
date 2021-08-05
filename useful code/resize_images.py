import shutil
import os
from PIL import Image

path_to_root = "/home/ghadeer/Projects/Datasets/RICOH_THETA/"
path_to_dist = "/home/ghadeer/Projects/Datasets/RICOH_THETA_resized/"

new_size = (512, 512)
names = os.listdir(path_to_root)
os.makedirs(path_to_dist, exist_ok=False)
for name in names:
    img = Image.open(path_to_root+name)
    new_img = img.resize(new_size)
    new_img.save(path_to_dist+name)

print("end")
