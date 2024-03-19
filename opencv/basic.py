#자르기 / 크기 조정
import cv2
import numpy as np

img = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(img) # 이미지 역상

print(img.shape) # (371, 640, 3)

cropped = img[50:200, 100:500]

resized = cv2.resize(cropped, (400, 200))

cv2.imshow("original", img)
cv2.imshow("dst", dst)
cv2.imshow("cropped", cropped)
cv2.imshow("resied", resized)

cv2.waitKey(0)
cv2.destoryAllWindows()