#pylint:disable=no-member

import cv2 as cv
import numpy as np
# contours and edges are mathematically different things
# contours are usefull for object recognition

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# mode in which to find contours in canny img
    # cv.RETR_TREE: all hirarchial contours
    # cv.RETR_EXTERNAL: only external contours (only the ones on the outside)
    # cv.RETR_LIST: all contours in the image
    # cv.RETR_FLOODFILL:
    # cv.RETR_CCOMP:
# Contour Approximation Method
    # None: All coordinates
    # SIMPLE: Compresses contours for example a line to only beginning- and end-coordinats 

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)

# Take away lessons:
    # 1. If a lot of contours are found in an image, it can be usefull to reduce data by blurring the image prior to finding contours
    # 2. Canny Edge and threshold can bring two different results, where threshold binarises the image
    # 3. drawing contours in a blank image to show found contours