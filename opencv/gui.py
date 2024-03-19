import cv2
import numpy as np

cap = cv2.VideoCapture(0)

topLeft = (50, 50)
bottomRight = (300, 300)

points = (200, 200)
def click(event, x, y, flags, param):
    global points, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x, y)
        points = (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        print("detach")

     


while(cap.isOpened()):
    ret, frame = cap.read()

    #Line
    cv2.line(frame, topLeft, bottomRight, (0, 255, 0), 5)

    #Rectangle
    cv2.rectangle(frame, [pt+30 for pt in topLeft], [pt+30 for pt in bottomRight], (0, 0, 255), 5)

    #circle
    cv2.circle(frame, points, 40, (155, 155, 155), 1)

    #text
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(frame, 'me', [pt+30 for pt in topLeft], font, 2, (0, 255, 255), 10)

    #display
    cv2.imshow("Camera", frame)

    cv2.setMouseCallback("Camera", click)

    key = cv2.waitKey(33)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()