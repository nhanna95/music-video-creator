# # importing libraries
# import os
# import cv2
# from PIL import Image

# # Checking the current directory path
# print(os.getcwd())

# # Folder which contains all the images
# # from which video is to be generated
# os.chdir("/Users/shreyagarwal/Code/GitHub/music-video-creator/folder")
# path = "/Users/shreyagarwal/Code/GitHub/music-video-creator/folder"

# mean_height = 0
# mean_width = 0

# num_of_images = len(os.listdir('.'))
# # print(num_of_images)

# for file in os.listdir('.'):
# 	im = Image.open(os.path.join(path, file))
# 	width, height = im.size
# 	mean_width += width
# 	mean_height += height
# 	# im.show() # uncomment this for displaying the image

# # Finding the mean height and width of all images.
# # This is required because the video frame needs
# # to be set with same width and height. Otherwise
# # images not equal to that width height will not get
# # embedded into the video
# mean_width = int(mean_width / num_of_images)
# mean_height = int(mean_height / num_of_images)

# # print(mean_height)
# # print(mean_width)

# # Resizing of the images to give
# # them same width and height
# for file in os.listdir('.'):
# 	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
# 		# opening image using PIL Image
# 		im = Image.open(os.path.join(path, file))

# 		# im.size includes the height and width of image
# 		width, height = im.size
# 		print(width, height)

# 		# resizing
# 		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
# 		imResize.save( file, 'JPEG', quality = 95) # setting quality
# 		# printing each resized image name
# 		print(im.filename.split('\\')[-1], " is resized")


# # Video Generating function
# def generate_video():
# 	image_folder = '.' # make sure to use your folder
# 	video_name = 'mygeneratedvideo.avi'
# 	os.chdir("/Users/shreyagarwal/Code/GitHub/music-video-creator/folder")
	
# 	images = [img for img in os.listdir(image_folder)
# 			if img.endswith(".jpg") or
# 				img.endswith(".jpeg") or
# 				img.endswith("png")]
	
# 	# Array images should only consider
# 	# the image files ignoring others if any
# 	print(images)

# 	frame = cv2.imread(os.path.join(image_folder, images[0]))

# 	# setting the frame width, height width
# 	# the width, height of first image
# 	height, width, layers = frame.shape

# 	video = cv2.VideoWriter(video_name, 0, 1, (width, height))

# 	# Appending the images to the video one by one
# 	for image in images:
# 		video.write(cv2.imread(os.path.join(image_folder, image)))
	
# 	# Deallocating memories taken for window creation
# 	cv2.destroyAllWindows()
# 	video.release() # releasing the video generated


# # Calling the generate_video function
# generate_video()

# import cv2
# import numpy as np
# import glob

# img_array = []
# for filename in glob.glob('/Users/shreyagarwal/Code/GitHub/music-video-creator/folder'):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)


# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()

# import ffmpeg
# import os

# os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4")

import os
import moviepy.video.io.ImageSequenceClip
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

image_files = []

for img_number in range(1,7): 
    image_files.append('/Users/shreyagarwal/Code/GitHub/music-video-creator/folder/thing' +str(img_number) + '.png') 

fps = 0.2

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('/Users/shreyagarwal/Code/GitHub/music-video-creator/folder' + 'my_new_video.mp4')