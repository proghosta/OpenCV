import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture('vlv.mp4')
frame = cap.read()[1]
frame = cv.resize(frame, (1280,720))

x, y, w, h = 554,279,100,37
track_window = (x,y,w,h)

roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)


term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
while 1:
    frame = cap.read()[1]
    frame = cv.resize(frame, (1280,720))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0,180], 1)
    ret, track_window = cv.CamShift(dst, track_window, term_crit)
    # x,y,w,h = track_window
    # final_image = cv.rectangle(frame, (x,y), (x+w, y+h), 255, 2)
    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    final_image = cv.polylines(frame, [pts], True, (0,255,0), 2)
    cv.imshow('dst', dst)
    cv.imshow('car', final_image)
    if cv.waitKey(400) == 27:
        break


cap.release()
cv.waitKey(0)
cv.destroyAllWindows()