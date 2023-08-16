import cv2 as cv
from cv2 import cvtColor
from cv2 import BORDER_DEFAULT

class convert_img_visuals:
    
    def grayscale(img):
        grayscaled_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return grayscaled_img
    
    def blur(img, blur = 3):
        #first argument is src image
        #second argument is a tuple containing a 'kernel size'
        #a kernel is the amount that is blurred
        #kernel size HAS TO BE odd size
        #third argument is
        blurred_img = cv.GaussianBlur(img, (blur, blur) , cv.BORDER_DEFAULT)
        return blurred_img