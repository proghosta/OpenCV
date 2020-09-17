import numpy as np
import cv2 as cv

def call_back(x):
    print(x)

cv.namedWindow('image')
switch = 'Color/Gray'
cv.createTrackbar('CP', 'image', 10, 400, call_back)
cv.createTrackbar(switch, 'image', 0, 1, call_back)


while 1:
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    cv.putText(img, str(pos), (50,150), cv.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 2)

    if s == 1:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('image', img)

    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()