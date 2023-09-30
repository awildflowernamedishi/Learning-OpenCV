import numpy as np
import cv2

img=cv2.imread('assets/chessboard.png')
img=cv2.resize(img, (0, 0), fx=0.4, fy=0.4) #resizing for convenience
grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale image is preferred

corners=cv2.goodFeaturesToTrack(grey, 100, 0.5, 10) #returns corners from the image
corners=np.int0(corners) #convert float-values returned in array to int
for corner in corners:
    x, y=corner.ravel() #flattens the array
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1) #draws a red-filled circle around detected corners

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1=tuple(corners[i][0])
        corner2=tuple(corners[j][0])
        color=tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) #generates random color and maps NumPy integers into Python lib int values
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Chess-Board', img)
cv2.waitKey(0)
cv2.destroyAllWindows()