import cv2
import numpy as np

# img1 = np.zeros((250,500,3), np.uint8)
# img2 = np.zeros((250,500,3), np.uint8)
# cv2.rectangle(img1, (200,0),(300,100), (255,255,255), -1)
# cv2.rectangle(img2, (250,0),(500,250),(255,255,255), -1)
img1 = cv2.imread('messi5.jpg')
img1 = cv2.resize(img1, (512,512))
img2 = cv2.imread('opencv-logo.png')
img2 = cv2.resize(img2, (512,512))
bitAnd = cv2.bitwise_not(img1)

cv2.imshow('img3', bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()