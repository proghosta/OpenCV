import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([640,480,3], np.uint8)
img = cv2.arrowedLine(img, (0,0), (255,255), (255,255,255), 10)
img  = cv2.rectangle(img, (20,20), (200,200), (255,255,255), 2)
img = cv2.circle(img, (110,110), 90, (255,255,255),  -1)
img = cv2.putText(img, 'Hello, World!', (40,113), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()