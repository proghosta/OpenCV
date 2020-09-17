import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
# img = np.zeros((200,200), np.uint8)
# cv.rectangle(img, (0,100), (200,200), (255), -1)
# cv.rectangle(img, (0,50), (100,100), (127), -1)
# b,g,r = cv.split(img)
# cv.imshow('image', img)
# title = ['Blue', 'Green', 'Red']
# images = [b,g,r]
# for i in range(3):
#     plt.subplot(2,2,i+1)
#     plt.hist(images[i].ravel(), 256, [0,256])
#     plt.title(title[i])
hist = cv.calcHist([img], [0], None, [256], [0,256])

plt.plot(hist)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()