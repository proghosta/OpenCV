import numpy as np
import cv2 as cv

img = cv.imread('shapes.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5,5), 0)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1,20, param1 = 50, param2 = 30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))
for circle in detected_circles[0]:
    x,y,r = circle
    cv.circle(img, (x,y), r, (0,0,0), 2)
    cv.circle(img, (x, y), 2, (255,)*3, 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()