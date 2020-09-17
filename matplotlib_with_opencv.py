import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', -1)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('image', img)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()