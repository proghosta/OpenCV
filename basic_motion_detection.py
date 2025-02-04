import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')
_, frame1 = cap.read()
_, frame2 = cap.read()


while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)
    contours = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 750:
            continue
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.putText(frame1, 'Status: Movement', (10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    # cv.drawContours(frame1, contours, -1, (0,255,0), 2)
    cv.imshow('feed', frame1)
    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break


cap.release()
cv.destroyAllWindows()