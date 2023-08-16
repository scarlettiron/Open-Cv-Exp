import cv2 as cv

class resize_rescale:
    def __init__():
        pass
    
    def rescale_frame(frame, scale_to=0.75):
        # to access width and height of frame use frame.shape
        # frame[0] is for height
        # frame[1] is for width
        print(scale_to)
        #make sure to cast as int
        new_height = int(frame.shape[0] * scale_to)
        new_width = int(frame.shape[1] *  scale_to)
        new_dimensions = (new_width, new_height)
        
        return cv.resize(frame, new_dimensions, interpolation = cv.INTER_AREA)
    
    #for rescaling and modifying resolution of live videos only  
    def change_live_resoltuion(capture, width, height):
        #3 references width
        #4 references height
        #10 references brightness
        capture.set(3, width)
        capture.set(4, height)
        return capture    
    
    #ignores image aspect ratio
    def crop_image(img, height, width):
         cropped_image = cv.resize(img, (height, width))
         return cropped_image