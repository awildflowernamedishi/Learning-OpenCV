import numpy as np
import cv2
cap=cv2.VideoCapture(0) #loads webcam feed
while True:
    ret, frame=cap.read() #captures and validates frame from feed
    width=int(cap.get(3)) #width of frame; property id=3
    height=int(cap.get(4)) #height of frame; property id=4
    img=np.zeros(frame.shape, np.uint8) #creates canvas of the same shape of our captured frame with the type of array values
    shrunk_frame=cv2.resize(frame, (0,0), fx=0.5, fy=0.5) #shrinking height and width of frame by half
    img[:height//2, :width//2]=cv2.rotate(shrunk_frame, cv2.ROTATE_180) #paste in top left
    img[height//2:, :width//2]=shrunk_frame #paste in bottom left
    img[:height//2, width//2:]=cv2.rotate(shrunk_frame, cv2.ROTATE_180) #paste in top right
    img[height//2:, width//2:]=shrunk_frame #paste in bottom right
    cv2.imshow('Captured-Frame', img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release() #releases webcam
cv2.destroyAllWindows()