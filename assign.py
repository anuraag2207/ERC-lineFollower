import cv2
import numpy as np

img=cv2.imread('line_detection.jpg')

cv2.imshow("path", img)
img1=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img2=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Yellow
low_yellow=np.array([15,20,128])
up_yellow=np.array([35,255,255])
yellow_mask= cv2.inRange(img1, low_yellow, up_yellow)
yellow=cv2.bitwise_and(img1, img1, mask=yellow_mask)
cv2.imshow('path2', yellow)
#white
low_white=np.array([143,148,161])
up_white=np.array([223,232,233])
white_mask= cv2.inRange(img2, low_white, up_white)
white=cv2.bitwise_and(img2, img2, mask=white_mask)
cv2.imshow('path3', white_mask)
cv2.waitKey(0)
