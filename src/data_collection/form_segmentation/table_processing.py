import cv2
import numpy as np

import image_processing as img_proc

def draw_contours(img, rectangles):
	"""
	Input:
	  raw color image
	  list of minAreaRect around the target objects
	Output:
	  color image with drawn contours around the target objects
	"""
	res = img.copy()

	for rect in rectangles:
		box = cv2.boxPoints(rect)
		box = np.int0(box)	
		cv2.drawContours(res,[box],0,(0,255,0),3)
	
	return res

def warp_img_backward(raw_img, rect):
	"""
	This function estimates the warp of raw_img based on the rect and
	warps is backward

	Input: 
	  raw_img - raw color image
	  rect - minAreaRect of the target object 
	    (i.e. centroid, width, height, angle of rotation)
	Output: 
	  warped backward image
	"""
	angle = rect[2]
	if abs(angle)<45:
		center, width, height = rect[0], rect[1][0],rect[1][1]
	else:
		center, height, width = rect[0],rect[1][0],rect[1][1]
		angle = 90.0+angle
		
	x1,x2 = abs(int(center[0]-width*0.5)), abs(int(center[0]+width*0.5))
	y1,y2 = abs(int(center[1]-height*0.5)),abs(int(center[1]+height*0.5)) 	
	M = cv2.getRotationMatrix2D(center,angle,scale=1)
	dst = cv2.warpAffine(raw_img,M,(raw_img.shape[1], raw_img.shape[0]))

	return dst[y1:y2, x1:x2]

def get_cells(roi, min_cell_area):
	"""
	Input:
	  roi - region of interest
	  min_cell_area - a threshold, 
	    i.e. contours with area less than thr are discarded
	Output:
	  cnt_list - list of contours
	"""
	cnt_list = []
	# preprocess ROI
	gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
	thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,7,3)
	
	# extract contours	
	_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	
	# loop through all contours
	for i,cnt in enumerate(contours):
		area = cv2.contourArea(cnt)
		# consider only child contours with area over CELL_MIN_CONTOUR_AREA
		if (area>min_cell_area and hierarchy[0,i,-1]!=-1):
			rect = cv2.minAreaRect(cnt)
			box = cv2.boxPoints(rect)
			box = np.around(box)
			box = np.int0(box)
			startX,startY,endX,endY = box[:,0].min(),box[:,1].min(), box[:,0].max(), box[:,1].max()
			cnt_list.append(np.array((startX,startY,endX,endY)))

	return np.array(cnt_list)

def get_cell(img,box):
	"""
	This function returns the patch of the image defined by the box
	"""
	startX,startY,endX,endY = box

	return img[startY:endY, startX:endX]

def clean_cell(img,min_area_thresh=15):
	# preprocess ROI
	if (len(img.shape)==3):
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	else:
		gray = img.copy()

	thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,7,3)
	# extract contours	
	_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	contour_pixels = []
	for i,cnt in enumerate(contours):
		area = cv2.contourArea(cnt)
		if (area>min_area_thresh and hierarchy[0,i,-1]==-1):
			temp = cnt.reshape((cnt.shape[0],cnt.shape[2]))
			# do not consider tall-thin and wide-thin regions
			w = temp[:,0].max() - temp[:,0].min()
			h = temp[:,1].max() - temp[:,1].min()
			if (float(w)/h>0.2 and float(h)/w>0.2):
				contour_pixels.extend(temp)

	contour_pixels = np.array(contour_pixels)
	cleanImg = None
	if (contour_pixels.size):
		x1 = contour_pixels[:,0].min()
		x2 = contour_pixels[:,0].max()
		y1 = contour_pixels[:,1].min()
		y2 = contour_pixels[:,1].max()
		
		off = 1
		startX = x1-off if x1-off>=0 else 0
		startY = y1-off if y1-off>=0 else 0
		endX = x2+off if x2+off<=img.shape[1] else img.shape[1]
		endY = y2+off if y2+off<=img.shape[0] else img.shape[0]
		
		w = endX-startX
		h = endY-startY
		
		off=10
		if (len(img.shape)==3):
			cleanImg = np.ones((h+2*off,w+2*off,3))*255
		else:
			cleanImg = np.ones((h+2*off,w+2*off))*255
		cleanImg = cleanImg.astype(np.uint8)
		cleanImg[off:h+off, off:w+off] = img[startY:endY, startX:endX]
		#cleanImg = cv2.medianBlur(cleanImg,3)
		#cv2.imshow('3', cleanImg)
		#cv2.waitKey(0)
	
	return cleanImg

def align_coords(raw_cords, dist=10):
	"""	
	This function assigns pxl[i] for any pxl[j] that 
	satisfy the condition  abs(pxl[i]-pxl[j])<=dist
	
	Input: 
		(N,1) vector (np.array)
	Output: 
		(N,1) vector (np.array) 
	"""
	coords = raw_cords.copy()
	i=-1
	while True:
		uniqueCoords = np.unique(coords)
		i+=1
		if i>uniqueCoords.shape[0]-1:
			break
		m = uniqueCoords[i:].min()
		coords[(coords>m)&(coords<=m+dist)]=m
		
	return coords

def smooth_coords(raw_coords, dist=10):
	coords = raw_coords.copy()
	
	coords[:,0] = align_coords(coords[:,0],dist)
	coords[:,1] = align_coords(coords[:,1],dist)
	coords[:,2] = align_coords(coords[:,2],dist)
	coords[:,3] = align_coords(coords[:,3],dist)
	
	return coords

def recover_tbl_struct(unsorted_cells,row_min_cell_num):
	# sort cells, first, along x, then along y
	ind = np.lexsort((unsorted_cells[:,0], unsorted_cells[:,1]))
	sorted_cells = unsorted_cells[ind]

	uniqueY = sorted(set(sorted_cells[:,1]))
	rows = []
	for y in uniqueY:
		# list of a single row cells along x 
		temp = sorted_cells[sorted_cells[:,1]==y]
		# discard "empty" rows (rows with the number of cells <ROW_MIN_CELL_NUM)
		if temp.shape[0]>row_min_cell_num:
			rows.append(temp)

	return rows

def retrieve_tables(raw_img, tbl_min_cnt_area):
	"""
	Retrieve Regions Of Interest (ROIs)

	Input: 
	  raw_img - raw color image
	  tbl_min_cnt_area - a threshold, 
	    i.e. contours with area less than thr are discarded
	Output: 
	  list of table regions cut from the input image
	"""
	img = img_proc.threshold_img(raw_img)
	# Find all parent contours (level zero contours)
	_,contours,_ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	feasible_cnts = []
	for cnt in contours:
		area = cv2.contourArea(cnt)	
		if (area>tbl_min_cnt_area):
			print("Contour area %f"%(area))
			rect = cv2.minAreaRect(cnt)
			feasible_cnts.append(rect)
	tables = []
	for rect in feasible_cnts:	
		tbl = warp_img_backward(raw_img, rect)
		tables.append(tbl)

	return tables

if __name__ == "__main__":
	import os
	IMG_PATH = 'imgs/'
	#fNames = os.listdir(IMG_PATH)
	fNames = ['1.jpg','2.jpg']
	for fn in fNames:
		print (fn)
		fname = os.path.join(IMG_PATH,fn)
		img = cv2.imread(fname)
		clean_cell(img)
		#txt = getCellContent(img,'6')
		#print (fn.split('.')[0].split('_')[-1], txt)