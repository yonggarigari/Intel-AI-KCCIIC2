import cv2
import numpy as np
img = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)

cv2.waitKey(0)

color = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)
print(color.shape)
height, width, channels = color.shape

cv2.imshow("original", img)

b, g, r = cv2.split(color)
rgb_split = np.concatenate((b,g,r), axis = 1)
cv2.imshow("BGR channels", rgb_split)
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis = 1)
cv2.imshow("hsv channels", hsv_split)

cv2.waitKey(0)
cv2.destoryAllWindows()