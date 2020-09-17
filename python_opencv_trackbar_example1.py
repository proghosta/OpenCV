import numpy as np
import cv2 as cv

def call_back(x):
    print(x)

img = np.zeros((300,500,3), np.uint8)
cv.namedWindow('image')
cv.createTrackbar('B', 'image', 0, 255, call_back)
cv.createTrackbar('G', 'image', 0, 255, call_back)
cv.createTrackbar('R', 'image', 0, 255, call_back)
switch = 'On/Off'
cv.createTrackbar(switch, 'image', 0,1, call_back)
while 1:
    cv.imshow('image', img)
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()