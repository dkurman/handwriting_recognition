import cv2,os
import numpy as np
from matplotlib import pyplot as plt

def resize_image(img, trg_width):
	"""
	This function resizes the input img with the recommended interpolation settings:
	  shrinking - cv2.INTER_AREA 
	  zooming - cv2.INTER_CUBIC or cv.INTER_LINEAR 
	  cv2 default - cv2.INTER_LINEAR
	"""
	try:	
		h,w = img.shape
	except:
		h,w,_ = img.shape
	
	interpolation = cv2.INTER_LINEAR
	if (trg_width<w):
		interpolation = cv2.INTER_AREA
	trg_height = int(trg_width*h/w)

	return cv2.resize(img,(int(trg_width),int(trg_height)), interpolation=interpolation)

def show_scaled_img(title, img):
    """
    Scale the image and plot it
    """
    imS = resize_image(img, 640)

    cv2.imshow(title,imS)
    cv2.waitKey(0)

def blue_detection(img):
	"""
	Input: 
	  img - raw color image
	Output: 
	  mask - array of indeces of blue pixels
	"""
	# Convert BGR to HSV
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# define range of blue color in HSV
	lower_blue = np.array([90,30,50])
	upper_blue = np.array([135,255,255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	
	return mask

def threshold_img(img):
	"""
	This function prepares the image for table_detection process

	Input: 
	  img - raw color image
	Output: 
	  processed binary image
	"""	
	# remove additive noise
	blur = cv2.medianBlur(img,3)
	blur = cv2.GaussianBlur(blur,(3,3),5.0)
	
	# remove blue stamps
	mask = blue_detection(img)
	invMask = cv2.bitwise_not(mask)
	no_blue = blur.copy()
	no_blue[invMask==0] = (255,255,255)
	
	gray = cv2.cvtColor(no_blue,cv2.COLOR_BGR2GRAY)
	thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,7,3)
	closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_CROSS,(3,1)))

	# Save & display the intermediate results
	show_imgs = False
	if show_imgs:
		show_scaled_img('1: Original', img)
		show_scaled_img('2: Smoothed', blur)	
		show_scaled_img('3: Blue mask', mask)
		show_scaled_img('4: No blue', no_blue)
		show_scaled_img('5: Black & White',thresh)
		show_scaled_img('6: Closing',closing)
	
	return closing

def reinforce_empty_regions(raw_img,quantile=0.1):
	"""
	DOES NOT WORK AS EXPECTED (breaks the contours)
	This function 
		- finds the regions that have "no text" (vertical gaps)
		- sets all pixels of this regions to 255
	Input: 
		raw_img - an unprocessed image
		quantile - threshold (values lower than found by quantile value are set 0)
	"""
	img = threshold_img(raw_img)
	# count non-zero pixels along the y axis
	sum_of_cols = np.sum(img,axis=1)/255.0

	qval = np.quantile(np.unique(sum_of_cols),q=quantile, interpolation = 'midpoint')
	sum_of_cols[(sum_of_cols<=int(qval))] = 0
	#plt.plot(sum_of_cols)
	#plt.show()

	img  = raw_img.copy()
	img[sum_of_cols==0,:]=255

	return img


def pprocess_img(img):	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	_,thresh=cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
	smoothImage = cv2.medianBlur(thresh,5)
	
	edges = cv2.Canny(smoothImage,50,150,apertureSize = 3)
	
	kernel = np.ones((9,9),np.uint8)
	dilation = cv2.dilate(edges,kernel,iterations = 1)
	
	
	height, width = dilation.shape
	# erase artefacts on edges of the page
	# TEMP: hard coding offset from the edges (it may cause problems for heavily rotated images)
	cv2.rectangle(dilation,(0,0), (50,height), 0, cv2.FILLED)
	cv2.rectangle(dilation,(width-50,0), (width,height), 0, cv2.FILLED)
		
	return dilation

def append_line_to_list(coordinates, candidate_coordinate, thresh=10):
	'''
	The candidate line is added to the list of coordinates only if its distance to other lines greater than thresh
	'''
	appendToList = True
	for i in range(len(coordinates)):
		if np.abs(coordinates[i]-candidate_coordinate)<thresh:
			appendToList=False
			break
	return appendToList

verLineDistThresh = 30	#in pixels
horLineDistThresh = 220 #in pixels

def filter_form_lines(img, thresh=1000):
	lines = cv2.HoughLines(img,1,np.pi/180,thresh)
	height, width = img.shape
	y = []
	x = []
	for i in range(lines.shape[0]):
		for rho,theta in lines[i]:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + width*(-b))
			y1 = int(y0 + height*(a))
			x2 = int(x0 - width*(-b))
			y2 = int(y0 - height*(a))
			# theta is in radians
			if (np.abs(theta-0.5*np.pi)<0.01 or np.abs(theta)<0.01):
				# vertical lines theta=1; horizontal lines theta=0
				if int(theta)==1 and y1>0:
					appendY = append_line_to_list(y,y1,verLineDistThresh)
					if (appendY):	
						y.append(y1)
				elif int(theta)==0 and x1>0:
					appendX = append_line_to_list(x,x1,horLineDistThresh)
					if (appendX):	
						x.append(x1)
	return np.sort(x), np.sort(y)

def segment_img(img,x,y,fname,crop_pxls=[15,15,15,15]):
	'''
	Image is segmented by straight lines crossing the entire image. 
	These lines are either vertical or horizontal. Therefore, each line is represented by a single coordinate x or y.
	A lot of hard coding is going here! It is a good idea to change unnamed constants to named ones.
	'''
	_, width,_ = img.shape
	for i in range(len(y)-1):
		cv2.imwrite(os.path.join("res/",str(i)+"_"+fname),img[y[i]+crop_pxls[0]:y[i+1]-crop_pxls[1],x[0]+crop_pxls[2]:x[1]-crop_pxls[3]])
		cv2.imwrite(os.path.join("res/",str(i+21)+"_"+fname),img[y[i]+crop_pxls[0]:y[i+1]-crop_pxls[1],x[2]+crop_pxls[2]:width-crop_pxls[3]])