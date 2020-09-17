import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg', 0)
th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)[1]
th2 = cv.threshold(img, 127,255, cv.THRESH_TRUNC)[1]
th3 = cv.threshold(img, 127,255, cv.THRESH_TOZERO)[1]
th4 = cv.threshold(img, 127,255, cv.THRESH_OTSU)[1]
th5 = cv.threshold(img, 127,255, cv.THRESH_TOZERO_INV)[1]
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

# cv.imshow('image', img)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
plt.show()
