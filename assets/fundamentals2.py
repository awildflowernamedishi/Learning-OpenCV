import cv2
import random
img=cv2.imread('assets/bastion-logo.png') #loads without transparency
tag=img[100:300, 349:499] #copy part of image
img[:200, 250:400]=tag #paste part of image
cv2.imshow('Bastion-Logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()