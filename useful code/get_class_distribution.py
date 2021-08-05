import os
import numpy as np
import PIL.Image as Image

split = "train"

classes = ["All_Optical", "Floor", "Glass", "Mirror", "Other optical surface"]

pth_to_class = {}

for class_ in classes:
   pth_to_class[class_] = split + "/" + class_ + "/" 
pth_save = split

images = [name for name in os.listdir(pth_to_class["Glass"])]

temp_img = Image.open(pth_to_class["Glass"] + images[0])
temp_img = temp_img.convert("L")
temp_arr = np.array(temp_img)
arr_size = temp_arr.shape

sum_pixels = {}
for class_ in classes:
    sum_pixels[class_] = np.zeros(arr_size)

for name in images:
    for class_ in classes:
        img = Image.open(pth_to_class[class_] + name)
        img = img.convert("L")
        arr = np.array(img)/255.0
        sum_pixels[class_] = np.add(arr, sum_pixels[class_])


for class_ in classes:
    sum_pixels[class_] = 255*(sum_pixels[class_]/np.max(sum_pixels[class_]))
    img = Image.fromarray(sum_pixels[class_])
    img = img.convert("RGB")
    img.save(split+"_"+class_+".png")


