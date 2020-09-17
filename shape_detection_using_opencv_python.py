import numpy as np
import cv2 as cv

img = cv.imread('shapes.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thrash = cv.threshold(imgray, 240, 255, cv.THRESH_BINARY)[1]
contours = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)[0]

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0,0,0), 2)
    x = cv.boundingRect(approx)[0]
    y = cv.boundingRect(approx)[1]
    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x,y), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    elif len(approx) == 4:
        _, _, w, h = cv.boundingRect(approx)
        aspectratio = float(w)/h
        if 0.95 <= aspectratio <= 1.15:
            cv.putText(img, 'Sqaure', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        else:
            cv.putText(img, 'Rectangle', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv.putText(img, 'Pentagon', (x+80,y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)
    elif len(approx) == 10:
        cv.putText(img, 'Star', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)
    else:
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),2)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
