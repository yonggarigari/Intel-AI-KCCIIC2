import cv2
import numpy as np

cap = cv2.VideoCapture("/home/yong/opencv/soccer.mp4")

idx = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        print("Can't open")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0) 
        continue

    #Resize
    frame = cv2.resize(frame, (frame.shape[1]//2, frame.shape[0]//2))

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    
    
    if key & 0xFF == ord('q'):
        break
    #'c'입력 시 frame save
    if key & 0xFF == ord('c'):
        cv2.imwrite('capture_{}.jpg'.format(idx), frame)
        print("Capture saved as capture.jpg")
        idx  += 1


 
cv2.destroyAllWindows()
cap.release()
