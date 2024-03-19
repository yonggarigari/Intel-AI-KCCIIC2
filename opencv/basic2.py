#이미지 역상
import cv2
import numpy as np

img = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)
src = cv2.imread("/home/yong/opencv/라이언.jpg", cv2.IMREAD_COLOR)

cropped = src[50:200, 100:500]
resized = cv2.resize(cropped, (640, 371))

dst_not = cv2.bitwise_not(img) 
#dst_and = cv2.bitwise_AND(img, src)
dst_or = cv2.bitwise_or(img, resized)
dst_xor = cv2.bitwise_xor(img, resized)

print(img.shape) # (371, 640, 3)


cv2.imshow("original", img)
cv2.imshow("ryon", resized)
cv2.imshow("dst_not", dst_not)
#cv2.imshow("dst_and", dst_and)
cv2.imshow("dst_or", dst_or)
cv2.imshow("dst_xor", dst_xor)


cv2.waitKey(0)
cv2.destoryAllWindows()