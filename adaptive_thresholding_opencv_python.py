import numpy as np
import cv2 as cv

img = cv.imread('sudoku.png', 0)
th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.waitKey(0)
cv.destroyAllWindows()