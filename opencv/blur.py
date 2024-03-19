import cv2

src = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)

dst = cv2.blur(src, (10, 10), anchor = (-1, -1), borderType=cv2.BORDER_REFLECT)


cv2.imshow("origin", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destoryAllWindows()