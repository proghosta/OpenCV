from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
cap = cv.VideoCapture(0)

# lap = cv.Laplacian(img, cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
# sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
#
# sobelX = np.uint8(np.absolute(sobelX))
# sobelY = np.uint8(np.absolute(sobelY))
# soblecombined = cv.bitwise_or(sobelX, sobelY)
# titles =  ['Image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined']
# images = [img, lap, sobelX, sobelY, soblecombined]

# for i in range(5):
#     plt.subplot(2, 3,i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
while 1:
    frame = cap.read()[1]
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
    sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)

    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    soblecombined = cv.bitwise_or(sobelX, sobelY)
    cv.imshow('image', soblecombined)
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()