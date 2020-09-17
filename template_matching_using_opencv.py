import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('tem.jpg', 0)
res = cv.matchTemplate(gray, template, cv.TM_CCORR_NORMED)
threshold = 0.99
loc = np.where(res >= threshold)
print(loc)
h, w = template.shape
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
