import cv2
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
    source_cv = cv2.imread(path_to_images+name)
    target_semantic_cv = cv2.imread(path_to_res+n[0]+".png")

    res = cv2.addWeighted(source_cv, 0.9, target_semantic_cv, 0.7, 0)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

    # cv2.imshow('dresst', res)
    res_img = Image.fromarray(res)
    res_img.save(os.path.join(path_to_merged, name[:-4]+".png"))





