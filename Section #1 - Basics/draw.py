#pylint:disable=no-member

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') # create empty image as np.zeros((height, width, colorchannels))
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# white:
blank[:50, :50] = 255,255,255 # [X (Spalte), Y(Zeile)] color code: B, G, R
# blue:
blank[50:200, 50:200] = 255,0,0 # color code: B, G, R
# green:
blank[50:200, 200:350] = 0,255,0 # color code: B, G, R
# red:
blank[50:200, 300:] = 0,0,255 # color code: B, G, R

#some colorful checkers
for i in range(0,5):
    for j in range(0,5):
        x1 = i*100
        x2 = (i+1)*100
        y1 = j*100
        y2 = (j+1)*100
        blank[x1:x2, y1:y2] = x1,y1,x2*y2    
        # print(x1,x2,y1,y2)

# cv.imshow('Colors', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (12,152,90), thickness=-1)
# cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (40,200,230), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (125,126,90), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Zneroke!!!', (0,30), cv.FONT_HERSHEY_TRIPLEX, .85, (50,80,120), 1)
cv.imshow('Text', blank)

cv.waitKey(0)