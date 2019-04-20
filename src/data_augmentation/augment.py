import cv2
import numpy as np
import os, glob
import random
from random import randint

import detect_word
import noise

# put cropped image into template image with random position
def random_position(small_image, big_image):
    H,W = big_image.shape
    h,w = small_image.shape
    x_range = W-w
    y_range = H-h
    x_pos = randint(0,x_range)
    y_pos = randint(0,y_range)
    big_image[y_pos:y_pos+h,x_pos:x_pos+w] = small_image
    
    return big_image

# main function with generate image from single image
def preproc_img(img):
    thresh = detect_word.basic_preprocessing(img)
    x,y,w,h = detect_word.find_bbox(thresh)

    new_img = np.ones((destination_size[0],destination_size[1]),dtype=np.uint8)*255
    new_img = random_position(img[y:y+h,x:x+w],new_img)
    new_img = noise.add_gaussian_noise(new_img,25)
    
    return new_img

if __name__ == "__main__":
    # folder of classes folders with images
    input_folder = "input_images" 
    # results will be saven in this folder
    output_folder = "generated_images" 
    #number of classes 
    classes = 10 
    # how many images will be created from each input image
    augmentation_number = 10 
    # output image size
    destination_size = (128,1024) 
    # height of word in output image
    word_height = int(destination_size[0]/2) 

    # чтение оригинального файла, аугментация и сохранение
    dataset = input_folder
    for c in range(0,classes):
        class_dir = os.path.join(dataset,str(c))
        all_files = glob.glob(class_dir+"/*.jpg")
        
        for j, full_path in enumerate(all_files):
            file = os.path.basename(full_path)
            img = cv2.imread(full_path)
            for i in range(augmentation_number):
                new_img = preproc_img(img)
                # cv2.imshow("test",new_img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                # break
                directory = output_folder+"/"+str(c)+"/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                cv2.imwrite(directory+file[:-4]+str(i)+file[-4:],new_img)


