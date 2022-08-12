import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv.line(frame, (0,0), (width, height), (0,255,0), 10)
    img1 = cv.line(img, (width,0), (0, height), (0,255,0), 10)
    imgR = cv.rectangle(img1, (100,100), (width-100,height-100), (255,255,255), 5)

    cv.imshow("webCam", imgR)

    key = cv.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()


