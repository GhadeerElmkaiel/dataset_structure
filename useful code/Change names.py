import shutil
import os

path_to_root = "images/test/"
path_to_dist = "edited_names/test/"
path_to_images = "images/test/images/"
# path_to_semantic = "images/train/Semantic/"

# path_to_new_images = "edited_names/train/images/"
# path_to_new_semantic = "edited_names/train/Semantic/"
folders = os.listdir(path_to_root)


names = os.listdir(path_to_images)
for folder in folders:
    os.makedirs(path_to_dist+folder,exist_ok=True)
    for name in names:
        new_name = str(10000+int(name[:-4]))+name[-4:]
        shutil.copy(path_to_root+folder+"/"+name, path_to_dist+folder+"/"+new_name)

print("end")