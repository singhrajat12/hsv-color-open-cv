'''import cv2
cap = cv2.VideoCapture(0)

while(1):
    _ , frameinv = cap.read()
    frame = cv2.flip(frameinv,1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("Frame", hsv)

    k = cv2.waitKey(10) & 0xFF

    if k ==27:
        break
cap.release()
cv2.destroyAllWindows()'''


import cv2
import numpy as np

def nothing(x):
    pass

kernel = np.zeros((300,512,3), np.uint8)
name = 'Calibrate'

cv2.namedWindow(name)

cv2.createTrackbar("hue", name , 0, 255, nothing)
cv2.createTrackbar("sat", name , 0, 255, nothing)
cv2.createTrackbar("val", name , 0, 255, nothing)

switch = "0 : OFF \n 1: ON"
cv2.createTrackbar(switch, name , 0, 1, nothing)

while(1):
    cv2.imshow(name, kernel)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

    hue = cv2.getTrackbarPos("hue", name)
    sat = cv2.getTrackbarPos("sat", name)
    val = cv2.getTrackbarPos("val", name)

    if switch == 0:
        kernel[:] = 0

    else:
        kernel[:] = [hue,sat,val]
cv2.destroyAllWindows()        
