from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('LinuxLogo.jpg', 0)
mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)[1]
kernal = np.ones((4,4), np.uint8)
dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
tophat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)
blackhat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernal)
hitmiss = cv.morphologyEx(mask, cv.MORPH_HITMISS, kernal)
rect = cv.morphologyEx(mask, cv.MORPH_RECT, kernal)
ellipse = cv.morphologyEx(mask, cv.MORPH_ELLIPSE, kernal)


titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat', 'blackhat', 'hitmiss', 'rect', 'ellipse']
images = [img, mask, dilation, erosion, opening, closing, gradient, tophat, blackhat, hitmiss, rect, ellipse]

for i in range(12):
    plt.subplot(3, 4,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()