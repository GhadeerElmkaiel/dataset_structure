import shutil
import os

path_to_root = "/home/ghadeer/Projects/Datasets/Sber2400/train/"
path_to_dist = "/home/ghadeer/Projects/Datasets/SberMerged/train/"
path_to_images = "/home/ghadeer/Projects/Datasets/Sber2400/train/images/"
# path_to_semantic = "images/train/Semantic/"

# path_to_new_images = "edited_names/train/images/"
# path_to_new_semantic = "edited_names/train/Semantic/"
files = os.listdir(path_to_dist)
folders = [x for x in files if "." not in x]


names = os.listdir(path_to_images)
for folder in folders:
    os.makedirs(path_to_dist+folder,exist_ok=True)
    for name in names:
        new_name = str(10000+int(name[:-4]))+name[-4:]
        # shutil.copy(path_to_root+folder+"/"+name, path_to_dist+folder+"/"+new_name)
        shutil.copy(path_to_root+folder+"/"+name, path_to_dist+folder+"/"+name)

print("end")
