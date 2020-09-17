import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

cap = cv.VideoCapture('roaddrive.mp4')

def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(image, mask)
    return masked_image

# frame = cap.read()[1]
# print(frame.shape)
# frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
# plt.imshow(frame)
# plt.show()

while cap.isOpened():
    image = cap.read()[1]
    # image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (1, 300),
        (300,242),
        (331, 244),
        (469, 358)
    ]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 20)
    edges = cv.Canny(blur, 100, 200)
    cropped_image = region_of_interest(edges, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(cropped_image, 1, np.pi / 100, 100, minLineLength=100, maxLineGap=10)
    try:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    except:
        continue
    cv.imshow('imshow', image)
    if cv.waitKey(30) == 27:
        break

# image = cv.imread('road2.jpg')
# image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
# height = image.shape[0]
# width = image.shape[1]
# region_of_interest_vertices = [
#     (0,570),
#     (590, 290),
#     (1196, 568)
# ]
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray, (7,7), 0)
# edges = cv.Canny(blur, 0, 200)
# cropped_image = region_of_interest(edges, np.array([region_of_interest_vertices], np.int32))
#
# lines = cv.HoughLinesP(cropped_image, 6, np.pi/60,160,  minLineLength=40, maxLineGap=25)
# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv.line(image, (x1,y1), (x2,y2), (0,255,0), 2)
#
#
# plt.imshow(image)
# plt.show()
cap.release()
cv.destroyAllWindows()