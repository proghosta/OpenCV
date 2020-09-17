import cv2 as cv
import numpy as np
img = cv.imread('lena.jpg')
img = cv.resize(img, (600,600))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 500, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img, (x,y), 3, 255, -1)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

