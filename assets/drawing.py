import numpy as np
import cv2
cap=cv2.VideoCapture(0) #loads webcam feed
while True:
    ret, frame=cap.read() #captures and validates frame from feed

    width=int(cap.get(3)) #width of frame; property id=3
    height=int(cap.get(4)) #height of frame; property id=4

    img=cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10) #draws blue line 10px thick from the top left corner to the bottom right corner of the webcam feed image
    img=cv2.line(img, (0,height), (width, 0), (0, 0, 255), 7) #draws red line 10px thick from the bottom left corner to the top right corner over the new img

    img=cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), -1) #draws a gray filled rectangle

    img=cv2.circle(img, (height//2, width//2), 60, (0, 255, 0), 5) #draws a green circle 5px thick in the centre of the webcam feed image

    img=cv2.putText(img, 'It\'s me, Hi! I\'m the problem, it\'s me.', (200, height-10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 7,   cv2.LINE_AA) #puts text on the webcam feed img

    cv2.imshow('Captured-Frame', img)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release() #releases webcam
cv2.destroyAllWindows()