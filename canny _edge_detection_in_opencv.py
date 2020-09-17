from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
def nothing(x):
    pass


img = cv.imread('messi5.jpg', 0)
cv.namedWindow('image')
cv.createTrackbar('Th1', 'image', 0, 300, nothing)
cv.createTrackbar('Th2', 'image', 0, 300, nothing)

while 1:
    th1 = cv.getTrackbarPos('Th1', 'image')
    th2 = cv.getTrackbarPos('Th2', 'image')
    canny = cv.Canny(img, th1, th2)
    cv.imshow('image', canny)
    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()