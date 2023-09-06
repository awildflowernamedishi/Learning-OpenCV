import cv2
import random
img=cv2.imread('assets/bastion-logo.png') #loads without transparency
for i in range(100): #first 100 rows of image
    for j in range(img.shape[1]): #corresponding columns in image
        img[i][j]=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] #random value of BGR
cv2.imshow('Bastion-Logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()