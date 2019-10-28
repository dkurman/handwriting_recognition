import os
import cv2
import numpy as np

import misc
from crop import crop
from scan import scan

# parameter initialization
# IMAGE_DIR = './imgs/'
# RESULT_DIR = './res/'
#
# if not os.path.exists(RESULT_DIR):
#     os.makedirs(RESULT_DIR)
#
# img_names = misc.get_file_names(IMAGE_DIR)

imgname = './imgs/20190925_33.jpg'
show_intermediate_results = True
scan(imgname, show_intermediate_results)
im = cv2.imread('deskewed.jpg')
im = cv2.dilate(im, np.ones((2, 2)))
newimgname = 'no_noise.jpg'
cv2.imwrite(newimgname, im)
crop(newimgname, 'scan_res.jpg', show_intermediate_results)

# img = cv2.imread('./imgs/20190925_33.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.GaussianBlur(img, (5,5), 0)

# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
# laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
# canny = cv2.Canny(img, 100, 150)
#
# cv2.imshow("Image", img)
# cv2.imshow("Sobelx", sobelx)
# cv2.imshow("Sobely", sobely)
# cv2.imshow("Laplacian", laplacian)
# cv2.imshow("Canny", canny)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# for filename in os.listdir(IMAGE_DIR):
# 	if filename.endswith(".png") or filename.endswith(".jpg"):
# 		img_name = os.path.join(IMAGE_DIR, filename)
# 	else:
# 		continue
# 	print ('\n%s'%(img_name))