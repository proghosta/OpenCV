import numpy as np
import cv2 as cv

img = cv.imread('opencv-logo.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh = cv.threshold(imgray, 127, 255, 0)[1]
contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)[0]
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow('Image', img)
cv.imshow('Gray', imgray)
cv.waitKey(0)
cv.destroyAllWindows()

