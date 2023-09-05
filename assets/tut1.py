import cv2
# img=cv2.imread('assets/bastion-logo.png', 0) #loads in grayscale
# img=cv2.imread('assets/bastion-logo.png', -1) #loads in normal color
img=cv2.imread('assets/bastion-logo.png', 1) #loads with transparency
# img=cv2.resize(img, (400, 400)) #resizes image dimensions by setting height and width of pixels
img=cv2.resize(img, (0, 0), fx=1.5, fy=1.5) #resizes image dimensions by multiplying dimensions of image by a natural or floating-point number
# img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #rotates image 90 degress clockwise
img=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #rotates image 90 degress anti-clockwise
cv2.imwrite('new-bastion-logo.png', img) #stores modified image into new-bastion-logo.png
cv2.imshow('Bastion-Logo', img)
cv2.waitKey(0)
cv2.destroyAllWindows()