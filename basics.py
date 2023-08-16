import cv2 as cv
from cv2 import VideoCapture
from resize_rescale_utils import resize_rescale as rr

#image from scr folder to be processed
''' img = cv.imread('/path/to/image')
cv.imshow('name', img) '''
#kills read when needed
#takes in arguments for milliseconds, 0 reads infinitely
#cv.waitKey(0)




#video from src folder to be processed
#takes a path to local video src 
#or arguments 0,1,2 etx for camera's hooked up
capture = VideoCapture('add ip url here')
check = capture.isOpened() 
print(check)
#read video frame by frame
while True:
    # isTrue returns boolean value if frame was succesfully read
    #frame is the actual frame instance
    isTrue, frame = capture.read()
    #resize frame to ease computer computation strain
    #resized_frame = rr.rescale_frame(frame, scale_to = 0.25)
    
    
    #cv.imshow('video', resized_frame)
    cv.imshow('or', frame)
    #end video when needed
    #0xff == ord('x') means when d is pressed
    if cv.waitKey(20) & 0xff==ord('x'):
        break

#MAKE SURE to free pointer and destroy all framse
capture.release()
cv.destroyAllWindows()   
