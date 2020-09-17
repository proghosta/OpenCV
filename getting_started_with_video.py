import cv2 as cv

cap = cv.VideoCapture(1)
four_cc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', four_cc, 24.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        out.write(frame)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == 27:
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
