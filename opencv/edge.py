import cv2

src = cv2.imread("/home/yong/opencv/straberry.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
canny = cv2.Canny(gray, 100, 200)
laplacian = cv2.Laplacian(gray, cv2.CV_8U)

cv2.imshow("opigin", gray)
cv2.imshow("Sobel", sobel)
cv2.imshow("Canny", canny)
cv2.imshow("lap", laplacian)

cv2.waitKey(0)
cv2.destoryAllWindows()