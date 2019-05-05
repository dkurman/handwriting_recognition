import cv2
import numpy as np
import os, glob
import random
from random import randint

import detect_word
import noise

# put cropped image into template image with random position
def random_position(small_image, big_image):
    # TODO: the small_image shall be resized so that to fit the big_image 
    # the function breaks when the big_image shape is (64,512)
    assert(small_image is not None and len(small_image.shape)<3)
    assert(big_image is not None and len(big_image.shape)<3)

    H,W = big_image.shape
    h,w = small_image.shape
    x_range = W-w
    y_range = H-h
    x_pos = randint(0,x_range)
    y_pos = randint(0,y_range)
    big_image[y_pos:y_pos+h,x_pos:x_pos+w] = small_image
    
    return big_image

# main function with generate image from a single image
def preproc_img(img, trg_size=(128,1024)):
    new_img = np.ones(trg_size,dtype=np.uint8)*255
    x,y,w,h = 0,0,img.shape[1],img.shape[0]

    thresh = detect_word.basic_preprocessing(img)
    bb = detect_word.find_bbox(thresh)
    if (bb):
        x,y,w,h = bb
    new_img = random_position(img[y:y+h,x:x+w],new_img)
    sigma = randint(0,50)
    new_img = noise.add_gaussian_noise(new_img, sigma)
    
    return new_img

if __name__ == "__main__":
    INPUT_IMG_DIR = "../../data/words_in_dirs"
    OUTPUT_IMG_DIR = "../../data/augmented_images"
    
    classes = 41
    aug_number = 10 
    trg_size = (128,1024)
    
    for c in range(0,classes):
        class_dir = os.path.join(INPUT_IMG_DIR,str(c))
        all_files = glob.glob(class_dir+"/*.jpg")
        print("Class: %d" % (c))
        
        for j, full_path in enumerate(all_files):
            fn = os.path.basename(full_path)
            img = cv2.imread(full_path,0)
            for i in range(aug_number):
                new_img = preproc_img(img,trg_size)
                
                directory = OUTPUT_IMG_DIR+"/"+str(c)+"/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                # TEMP: while small_image and big_image are not aligned
                new_img = cv2.resize(new_img, None, fx=0.5, fy=0.5)
                cv2.imwrite(directory+fn[:-4]+str(i)+fn[-4:], new_img)