import cv2 as cv
import numpy as np

#create a blank image
#first argument is size of image (height, width, number of color channels)
#second argument is datatype
#uint8 is an image data type
blank = np.zeros((500, 500, 3), dtype='uint8')

#first is image to draw on
#second is mapping from origin
#third is mapping to 
#fourth is rgb values of rectangle color
#fifth is rectangle thickness
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=-1)

cv.imshow('blank', blank)


cv.waitKey(0)