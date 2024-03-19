import cv2
import numpy as np

src = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(src)
inverse = cv2.merge((r, g, b))
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]

height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype = np.uint8)
bgz = cv2. merge((b, g, zero))


cv2.imshow("origin", src)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inverse)
cv2.imshow("bgz", bgz)

cv2.waitKey(0)
cv2.destoryAllWindows()