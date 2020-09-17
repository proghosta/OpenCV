import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv.createBackgroundSubtractorKNN()

while 1:
    frame = cap.read()[1]
    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv.imshow('frame', frame)
    cv.imshow('another_frame', fgmask)
    if cv.waitKey(40) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()