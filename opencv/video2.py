import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# 동영상 해상도 확인하기
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("동영상 해상도: {} x {}".format(width, height))

#동영상 해상도 변경하기
w = 1920
h = 1080

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = 'output.mp4'
fps = 30
out = cv2.VideoWriter(output_file, fourcc, fps, (w, h))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        print("Can't open")
        break

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
