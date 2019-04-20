import numpy as np
import cv2
import os
    
# In order to find the region of the word, the contour detection method is used

MIN_CONTOUR_AREA = 10

def basic_preprocessing(img):
    blur = cv2.GaussianBlur(img, (3, 3), 0)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,200)

    if False:
        cv2.imshow('Edges', edges)
        cv2.waitKey(0)

    return edges

def find_bbox(imgray, thresh_area=10):
    """
    The method expects a gray scale image
    It outputs the bbox = {x,y,w,h}
    """
    h,w = imgray.shape
    im2, contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print('Total # of contours: ', len(contours))
    
    # loop through all contours
    feasible_contours = []
    for i,cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        # consider only child contours with area over MIN_CONTOUR_AREA and 
        # less than 75% of the image area
        if (area>MIN_CONTOUR_AREA and area<(0.75*h*w)):
            feasible_contours.extend(cnt)

    bbox = cv2.boundingRect(np.array(feasible_contours))
    return bbox

def show_contours(img, contours):
    cv2.drawContours(img, np.array(contours), -1, (0,255,0), 1)
    cv2.imshow('Contours', img)
    cv2.waitKey(0)

def show_bbox(img, bbox):
    x,y,w,h = bbox
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
    cv2.imshow('Contours', img)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    IMG_DIR = "../data/words/"
    if False:
        file_names = os.listdir(IMG_DIR)
    else:
        file_names = ['0_20190124 001.jpg', '0_20190124 012.jpg','1_20190124 153.jpg']
    
    print("Number of files: ", len(file_names))
    print("Average shape of images: ", img_avg_shape(file_names))

    for fn in file_names:
        img = cv2.imread(os.path.join(IMG_DIR,fn))
        thresh = basic_preprocessing(img)
        bbox = find_bbox(thresh,thresh_area=MIN_CONTOUR_AREA)
        if True:
            show_bbox(img, bbox)