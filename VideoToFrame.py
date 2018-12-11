################################################################

# Python module and script for converting videos to images
#
# Can also be run as script by typing:
#
#	python VideoToFrame.py --p "path" 
#
# Where path is optional for videos on an outside directory
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

import ffmpeg
import os
import subprocess
import argparse

###############################################################################
dir_current = os.getcwd()

def vidToFrame(video_extension, desired_extension, dir_in=dir_current, dir_out='', framerate=25):
	'''

	Converts videos to frames. Takes the videos from dir_in and outputs the frames
	to the dir_out directory. *not coded for subdirectories*

	:param in_dir:
		Directory where video files are stored. ['C:\\Users\\Ivarg_000\\Desktop\\vidtoframe']

	:param out_dir:
		Directory where frames will be stored. ['/outputDirectory'] the slash is very important

	:param framerate:
		Integer. Frames per second rate desired. [25]

	:param video_extension:
		String. extension for video files in directory ['.mp4']

	:param desired_extension:
		String. Extension desired for output frames ['.jpeg']

	:return:
		None
	'''

	for video in os.listdir(dir_in):
		video_root, _ = os.path.splitext(video)
		if (video.endswith(video_extension)):
			str = 'ffmpeg -i {0} -r {1} {2}{3}_%03d{4}'
			# e.g. ffmpeg -i Crime-001.mp4 -r 0.25 vidz/vidz%05d.jpeg
			os.system(str.format(video, framerate, dir_out, video_root, desired_extension))
		else:
			continue

###############################################################################
# Script that allows the module to run from the command prompt

if __name__ == "__main__":
	
	description = "Convert video to frames. " \
	"Must specify the video file extension " \
	"as well as the output frame file extension. " \
	"All input videos must be in the current directory. " \
	"output frames are sent to the specified output directory. " \
	"the framerate is given as an argument of the function. "

	#parser creation
	parser = argparse.ArgumentParser(description=description)

	# Add the arguments to the parser
	parser.add_argument("--vidextension", required=True, 
		help="set video extension")

	parser.add_argument("--frameextension", required=True, 
		help="desired frame extension")

	parser.add_argument("--dirin", required=False, default=os.getcwd(),
		help="Input directory where videos are located")

	parser.add_argument("--dirout", required=False, default='',
		help="Output directory where frames will be sent to")

	parser.add_argument("--framerate", required=False, type=int, default=25,
		help="Frame per second conversion rate")

	args = parser.parse_args()

	ve = args.vidextension
	fe = args.frameextension
	di = args.dirin
	do = args.dirout
	fr = args.framerate

	print("Converting videos to images.")

	vidToFrame(video_extension=ve, desired_extension=fe, dir_in=di, dir_out=do, framerate=fr)
