#trackbar

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

topleft = (50, 50)
bold = 0
fontsize = 0
b, g, r = 0, 0, 0

def on_bold_Trackbar(value):
    global bold
    bold = value
def on_fontsize_Trackbar(value):
    global fontsize
    fontsize = value
def on_b_Trackbar(value):
    global b
    b = value
def on_g_Trackbar(value):
    global g
    g = value
def on_r_Trackbar(value):
    global r
    r = value

cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_Trackbar)
cv2.createTrackbar("size", "Camera", fontsize, 10, on_fontsize_Trackbar)
cv2.createTrackbar("b", "Camera", b, 255, on_b_Trackbar)
cv2.createTrackbar("g", "Camera", g, 255, on_g_Trackbar)
cv2.createTrackbar("r", "Camera", r, 255, on_r_Trackbar)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        print("fail")
        break

    #text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    #cv2.putText(frame, 'Test', topleft, font, 2, (0, 255, 255), 1+bold)
    cv2.putText(frame, 'Test', topleft, font, 1+fontsize, (b, g, r), 1+bold)

    #display
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(33)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()