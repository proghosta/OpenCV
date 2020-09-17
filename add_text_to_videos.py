import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))
cap.set(3, 3000)
cap.set(4, 3000)
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(int(cap.get(3))) + ' Height: ' + str(int(cap.get(4)))
        time = str(datetime.datetime.now())
        frame = cv2.putText(frame, time, (10,50), font, 1, (0,69,255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()