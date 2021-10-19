import cv2
import numpy as np
  
# reading image 
img = cv2.imread("img.jpg") # use your image here or use camera.

#cropping image
def rescaleFrame(frame,scale=0.50): # Adjust this scale between 0.00-1.00 for rescaling the image frame.
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # Then we setted dimensions as height asn width which we setted....
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    
# cv2.imshow('image', resized_image)
resized_image = rescaleFrame(img)
   
# Edges
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
edges = cv2.adaptiveThreshold(gray, 100, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                         cv2.THRESH_BINARY, 3, 3)
   
# Cartoonization
color = cv2.bilateralFilter(resized_image, 3, 50, 50)
cartoon = cv2.bitwise_and(color, color, mask=edges)
   
   
# cv2.imshow("Image", img)
# cv2.imshow("edges", edges)
cv2.imshow("Anime", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()