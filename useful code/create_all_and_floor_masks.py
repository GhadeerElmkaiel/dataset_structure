import os
import numpy as np
import PIL.Image as Image

path_to_labels = "/home/ghadeer/Projects/Datasets/Sber3500/images/train/"
pth_all = path_to_labels+"All_Optical/"
pth_floor = path_to_labels+"Floor/"
pth_save = path_to_labels+"All_and_Floor/"
os.makedirs(path_to_labels+'All_and_Floor', exist_ok=True)
images = [name for name in os.listdir(pth_all)]

for name in images:
    all_opt = Image.open(pth_all+name)
    floor = Image.open(pth_floor+name)

    all_opt = all_opt.convert("RGB")
    floor = floor.convert("RGB")

    arr_all = np.array(all_opt)
    arr_floor = np.array(floor)

    arr_floor[:,:,1:] = 0
    res = arr_floor + arr_all
    img = Image.fromarray(res)
    img.save(pth_save+name)

