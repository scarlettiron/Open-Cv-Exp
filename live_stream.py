
import cv2 as cv
from urllib.request import urlopen
import numpy as np



url = r'add ip url'
while True:
    #open url to view info
    stream_feed = urlopen(url)
    #read information from url, convert array into bytarray 
    imgnp = np.asarray(bytearray(stream_feed.read()), dtype="uint8")
    
    img = cv.imdecode(imgnp, -1)
    cv.imshow("Camera", img)
    if cv.waitKey(20) & 0xff == ord('x'):
        break
    
cv.destroyAllWindows()