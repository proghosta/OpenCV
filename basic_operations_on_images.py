import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img1 = cv2.imread('opencv-logo.png')
img = cv2.resize(img, (512,512))
img1 = cv2.resize(img1, (512, 512))
img3 = cv2.addWeighted(img,0.5, img1, 0.1,-100)

cv2.imshow('image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()