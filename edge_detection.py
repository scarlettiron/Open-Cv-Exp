import cv2 as cv
from cv2 import blur
from converting_img_visuals import convert_img_visuals as conv

class edge:
    
    def find_edges(img, threshold1 = 125, threshold2 = 125):
        #first is src image
        #second and third are threshold amounts
        edged_image = cv.Canny(img, threshold1, threshold2)
        return edged_image
    
    def find_reduced_edges(img, threshold = [125, 125], blur = 3):
        #first blur the image
        blurred_img = conv.blur(img, blur)
        #second convert image to edges
        edged_image = cv.Canny(img, threshold[0], threshold[1])
        return edged_image
    
    def dilate(img, dilate = 3, iterations = 3):
        #first argument is src image
        #second argument is a tuple containing a 'kernel size'
        #a kernel is the amount that is dilated
        #kernel size HAS TO BE odd size
        #third is number of iterations kernel is applied to image
        dilated_image = cv.dilate(img, (dilate, dilate), iterations=iterations)
        return dilated_image
    
    
    #first argument is src image
    #second argument is a tuple containing a 'kernel size'
    #a kernel is the amount that is eroded
    #kernel size HAS TO BE odd size
    #third is number of iterations kernel is applied to image
    def erode(img, erode, iterations):
        eroded_image = cv.erode(img, (erode, erode), iterations)
        return eroded_image
        
        
        
         