from PIL import Image
import glob
import re
import os
import numpy as np

mode = "test"
path_to_segmented_images = "/home/ghadeer/Projects/Datasets/Sber2400/"+mode+"/Semantic"
path_to_floor_labels_folders = "/home/ghadeer/Projects/Datasets/Sber2400/"+mode+"/All_Floor"
path_to_all_and_floor_labels_folders = "/home/ghadeer/Projects/Datasets/Sber2400/"+mode+"/All_and_Floor"
segmented_images = []

for img_path in glob.glob(path_to_segmented_images+'/*'):
    segmented_images.append(img_path)
os.makedirs(path_to_floor_labels_folders, exist_ok=True)

labels = open("labelmap.txt", "r")
# remove the header line from the file.
x = labels.readline()

# get the labels in the image with the corresponding color for each label
labels_dict = {}
for x in labels:
    x = re.split('[:]', x)
    name = x[0]
    vals = re.split('[,]', x[1])
    vals_int = [int(s) for s in vals]
    labels_dict[name] = vals_int

for class_ in labels_dict.keys():
    if class_ == "Trash" or class_ == "Background" or class_ == "background":
        continue


for img_path in segmented_images:
    img = Image.open(img_path)
    img_name = re.split('/',img_path)[-1]
    img_size = img.size
    img = img.convert("RGB")
    masks = {}
    for key in labels_dict.keys():
        if key == "Trash" or key == "Background" or key == "background":
            continue
        masks[key] = []
    all_optical = []
    datas = img.getdata()
    # print(masks.keys())


    img_np = np.array(img)[:,:,0]
    for key in masks.keys():
        masks[key] = np.array(img_np==labels_dict[key][0])
    glass_and_mirror = np.logical_or(masks["Glass"], masks["Mirror"])
    all_optical = np.logical_or(glass_and_mirror, masks["Other optical surface"])
    all_floor = np.logical_or(masks["Floor under obstacle"], masks["Floor"])


    curr_mask = Image.fromarray(all_floor)
    curr_mask = curr_mask.convert('1')
    curr_mask = curr_mask.convert('RGB')
    curr_mask.save(path_to_floor_labels_folders+"/"+img_name)
