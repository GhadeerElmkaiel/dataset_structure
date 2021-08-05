# Dataset Structure
For most of the used models, the main structre of the dataset for training and testing is very simple.  
it should contains three folders: **Train, Test, Validation**  
Each of them should contain **idealy** only two folders for images and masks. **(images, Semantic)**, but due to the different structures and codes for each model, there should be additional folders so the dataset works with all models.  
for example, for SegFormer, the mask images should be saved as palette, while for Trans2Seg should be saved as RGB images.
that is why there are currently two different folders with masks inside the dataset folders:
- Semantic: masks saved as RGB images
- Semantic_palette  
  
in the case of Trans2Seg there should be a palette image also named ```all_palette.png``` for training the Trans2Seg model on all different 6 classes.  
for training Trans2Seg models on all classes without **Floor Under Obstacles** we should add another palette image named ```all_no_fu_palette.png```  
Also for training Trans2Seg on **All optical** (as one classe) and **All floor** (as one class), another palette image should be added named as: ```optical_floor_palette.png```  
all palette images shuold contains all colors that will be used during training and testing.
 
so for training and testing most of the models (TransLab, Trans2Seg, SegFormer), the following dataset structure should work fine:  
Sber dataset
```  
├── all_palette.png  
├── all_no_fu_palette.png  
├── optical_floor_palette.png  
│
├── train  
│   ├── images  
│   ├── Semantic  
│   └── Semantic_palette  
├── test  
│   ├── images  
│   ├── Semantic  
│   └── Semantic_palette  
└── validation  
    ├── images  
    ├── Semantic  
    └── Semantic_palette  
```

for calculating metrics after the testing, I was using a separate folder for the masks of each class (so I don't need to process the full mask each time I calculate metrics)

so in **train, test, validation** folders there will be also the following folders:   
```
├── train  
│   ├── images  
│   ├── Semantic  
│   ├── Semantic_palette  
│   ├── All_Floor  
│   ├── All_Optical  
│   ├── Floor  
│   ├── Floor under obstacle  
│   ├── Glass  
│   ├── Glass_and_Mirrors  
│   ├── Mirror  
│   └── Other optical surface  
```
eahc of the new folders contains **colored or gray** masks of a specific class (**background= BLACK, the class=WHITE**)  

## Other useful codes
In this repository there are also different code files for different tasks, the main one is calculating metrics which can be found in the ```Metrics``` folder.   
another imprtant code is ```extract_masks.py``` which creates the masks for individual classes and for the additional combination of classes such ass ***(Glass_and_mirrors,  All_Optical, and All_Floor)***   
```get_class_distribution.py``` code is to represent the classes distribution in a dataset 
```add_mask_to_image.py``` code is to add a layer of color which represent the mask over the RGB image. 
```convert_images_to_palette.py``` code is to convert RGB images to palette (For SegFormer training).
