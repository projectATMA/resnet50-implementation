################################################################
# Python module and script for converting videos to processed images for ResNet50
#
# Can also be run as script by typing:
#
# Implemented in Python 3.5
#
# This file is used for IPMD's Project ATMA. Available at:
#
# https://github.com/projectATMA/resnet50-implementation
#
# Published under MIT License
#
###############################################################################

import VideoToFrame
from keras.applications import imagenet_utils
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
import numpy as np
import argparse

###############################################################################

#parameters
vidEx = '.mp4'
outputEx = '.jpeg'
inputDir=os.getcwd()
OutputDir=''
framerate=1

# Converts the videos to frames
VideoToFrame.vidToFrame(video_extension=vidEx,
	desired_extension=outputEx,
	dir_in=inputDir,
	dir_out=outputDir,
	framerate=framerate)


	for video in os.listdir(dir_in):
		video_root, _ = os.path.splitext(video)
		if (video.endswith(video_extension)):
			str = 'ffmpeg -i {0} -r {1} {2}{3}_%03d{4}'
			# e.g. ffmpeg -i Crime-001.mp4 -r 0.25 vidz/vidz%05d.jpeg
			os.system(str.format(video, framerate, dir_out, video_root, desired_extension))
		else:
			continue

# PROCESS THE VIDEOS BY USING THE ".JPEG" EXTENSION
inputShape = (224, 224) # image shape for ResNet50 model
preprocess = imagenet_utils.preprocess_input # pre processing module for imagenet images

'''
img_path = 'elephant.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
'''

for image in os.listdir(dir_in)

# MAYBE WE CAN USE THIS IMAGE PROCESSING INSIDE THE MODEL SCRIPT