# -*- coding: utf-8 -*-
import os
import cv2

import image_processing as img_proc
import table_processing as tbl_proc
import misc

# parameter initialization
IMAGE_DIR = './imgs/'
RESULT_DIR = './res/'

if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)

img_names = misc.get_file_names(IMAGE_DIR)

######################## TABLE_PROC_FREE_PARAMETERS #######################
TABLE_MIN_CONTOUR_AREA = 600000
ROW_MIN_CELL_NUM = 3
############################ END_FREE_PARAMETERS ##########################

for filename in os.listdir(IMAGE_DIR):
	if filename.endswith(".png") or filename.endswith(".jpg"): 
		img_name = os.path.join(IMAGE_DIR, filename)
	else:
		continue
	print ('\n%s'%(img_name))

	# load an input image
	img = cv2.imread(img_name)
	#img = img_proc.reinforce_empty_regions(img,quantile=0.08)

	# retrieve tables
	ROIs = tbl_proc.retrieve_tables(img,TABLE_MIN_CONTOUR_AREA)
	print("Number of tables: %d" %(len(ROIs)))

	# loop over all tables
	for k,roi in enumerate(ROIs):
		print ('\tROI_'+str(k)+': '+str(roi.shape))
		ppImg = img_proc.pprocess_img(roi)
		# get the list of horizontal and vertical lines
		x,y = img_proc.filter_form_lines(ppImg,1800)

		if (x.shape[0]==3 and y.shape[0]==22):
			img_proc.segment_img(roi,x,y,img_name.split('/')[2])
		print (x.shape, y.shape)
		height, width = ppImg.shape
		for i in range(len(y)):
			cv2.line(roi,(0,y[i]),(width,y[i]),(255,0,255),2)
		for i in range(len(x)):
			cv2.line(roi,(x[i],0),(x[i],height),(255,0,255),2)
		cv2.imwrite(os.path.join(RESULT_DIR,img_name.split('/')[2].split('.')[0]+ '_houghlines.png'),roi)
		
	if (False):
		img_proc.show_scaled_img('Original image',img)
		for i,roi in enumerate(ROIs):
			img_proc.show_scaled_img('Table #%d' %(i),roi)