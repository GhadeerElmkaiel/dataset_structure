
import glob
import re
import os
import shutil

path_to_masks = "Glass/"
path_to_rgb = "/home/ghadeer/Projects/Datasets/sber_ds/rgb_all/FullZedRGBDataset/"

images = []
for img in glob.glob(path_to_masks+'*'):
    name = re.split('[/]',img)[-1]
    shutil.copy(path_to_rgb+name, 'image/'+name)


