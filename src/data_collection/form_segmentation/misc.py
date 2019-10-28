import os
import numpy as np

def get_file_names(path):
	"""
	Input: path to the directory
	Output: list of files
	"""
	fnames = []
	if os.path.exists(path):
		fnames = os.listdir(path)
	else:
		print ('Directory does not exist: ', path)
	fnames.sort()
	return fnames


IMAGE_DIR = './imgs/'
files = get_file_names(IMAGE_DIR)
print(files)