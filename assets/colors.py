import numpy as np
import cv2
cap=cv2.VideoCapture(0) #loads webcam feed
while True:
    ret, frame=cap.read() #captures and validates frame from feed

    width=int(cap.get(3)) #width of frame; property id=3
    height=int(cap.get(4)) #height of frame; property id=4

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converts frame to hsv
    lower_bound=np.array([95,50, 50]) #lower bound of color in HSV color val to be extracted (light blue)
    upper_bound=np.array([130, 255, 255]) #upper bound of color in HSV color val to be extracted (darker blue)

    mask=cv2.inRange(hsv, lower_bound, upper_bound) #mask created to access pixels that fall in the specified range
    res=cv2.bitwise_and(frame, frame, mask=mask) #only the pixels match in the frame and mask will show

    cv2.imshow('Everything is blue!', res)
    cv2.imshow('Mask_demo', mask)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release() #releases webcam
cv2.destroyAllWindows()