import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
layer = img.copy()
gp = [layer]
# lr1 = cv.pyrDown(img)
# lr2= cv.pyrUp(lr1)
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
layer = gp[5]
for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)


# cv.imshow('image', img)
# cv.imshow('lr1', lr1)
# cv.imshow('lr2', lr2)

cv.waitKey(0)
cv.destroyAllWindows()