import numpy as np
import cv2

img=cv2.imread('assets/barbie_party.jpeg', 0) #loading base image in grayscale
template=cv2.imread('assets/ken_thumbs_up.PNG', 0) #loading template image in grayscale
height, width=template.shape #2D in grayscale image of the form (number of rows, number of columns)

methods=[cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] #different methods for template matching
for method in methods: #to try out all the methods and see which performs best
    img_cpy=cv2.resize(img.copy(), (0, 0), fx=0.25, fy=0.25) #to draw rectangle on detected object as per the method in the list
    #if there was no copy image, there would be many rectangles drawn on the original image based on the slightly varying results
    res=cv2.matchTemplate(img_cpy, template, method)
    min_value, max_value, min_loc, max_loc=cv2.minMaxLoc(res) #finding minimum and maximum values and locations
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location=max_loc
    #top left of rectangle is known
    bottom_right=(location[0]+width, location[1]+height)
    cv2.rectangle(img_cpy, location, bottom_right, 255, 4) #draw a white rectangle where the match is found
    cv2.imshow('It\'s a match', img_cpy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()