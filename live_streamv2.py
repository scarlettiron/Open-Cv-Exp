
import cv2
import numpy as np

url = r'add ip url here'

cap = cv2.VideoCapture(url)

while(cap.isOpened()):
    ret, image = cap.read()    
    loadedImage = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow('frame',loadedImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()