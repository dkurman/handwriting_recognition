import os
import glob
import numpy as np
import cv2

import imgaug as ia
from imgaug import augmenters as iaa

import detect_word

def preproc_img(img, trg_size=(64,512)):
    new_img = np.ones(trg_size,dtype=np.uint8)*255
    x,y,w,h = 0,0,img.shape[1],img.shape[0]

    thresh = detect_word.basic_preprocessing(img)
    bb = detect_word.find_bbox(thresh)
    if (bb):
        x,y,w,h = bb
    
    # center the word
    Y1, Y2 = int(0.5*trg_size[0]-0.5*h), int(0.5*trg_size[0]+0.5*h)
    X1, X2 = int(0.5*trg_size[1]-0.5*w), int(0.5*trg_size[1]+0.5*w)
    # get rid of rounding error
    Y1 = Y1 if ((Y2-Y1)-h==0) else Y1-((Y2-Y1)-h)
    X1 = X1 if ((X2-X1)-w==0) else X1-((X2-X1)-w)
    
    new_img[Y1:Y2,X1:X2] = img[y:y+h,x:x+w]
    
    return new_img

def compile_batch(img, batch_size):
    batch = []
    for i in range(batch_size):
        batch.append(img)
    
    batch = np.array(batch)

    return batch

def augment(batch):
    seq = iaa.Sequential([
        iaa.ElasticTransformation(alpha=30, sigma=11),  # water-like effect
        iaa.AdditiveGaussianNoise(scale=(1, 10)),
        iaa.Sometimes(0.5, iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}, # scale images to 80-120% of their size, individually per axis
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, # translate by -20 to +20 percent (per axis)
            rotate=(-5, 5), 
            shear=(-16, 16)
        )),
    ], random_order=True)
    
    images_aug = seq.augment_images(batch)

    return images_aug

def save_batch(output_dir, base_file_name, batch):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i, img in enumerate(batch):
        cv2.imwrite(directory + base_file_name[:-4] + str(i) + base_file_name[-4:], img)

def show_batch(batch):
    for img in batch:
        cv2.imshow("Augmented image", img)
        cv2.waitKey(0)

if __name__ == "__main__":
    INPUT_IMG_DIR = "../../../data/words_in_dirs"
    OUTPUT_IMG_DIR = "../../../data/imgaug_images"
    
    aug_number = 10
    classes = 42

    for c in range(0,classes):
        class_dir = os.path.join(INPUT_IMG_DIR,str(c))
        all_files = glob.glob(class_dir+"/*.jpg")
        print("Class: %d" % (c))
        for j, full_path in enumerate(all_files):
            fn = os.path.basename(full_path)
            img = cv2.imread(full_path,cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, None, fx=0.5, fy=0.5,interpolation=cv2.INTER_CUBIC)
            img = preproc_img(img)
            batch = compile_batch(img,aug_number)
            
            batch_aug = augment(batch)
            if False:
                show_batch(batch_aug)
            # save 
            directory = OUTPUT_IMG_DIR+"/"+str(c)+"/"
            save_batch(directory, fn, batch_aug)