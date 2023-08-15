#pylint:disable=no-member

import cv2 as cv

# blurring is used to reduce sensor noise in the image
# Concept of blurring:
    # Kernal/ Window:
    # - A Kernel is a portion or window of an image
    # - the kernel has a size of a single digit, eg 3
    # - a kernel of size 3 is a 3x3 grid
    # - this window slides around the image and sets values to the algorithms (gauss/ averaging/..) result

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging:
    # - Averaging sums up the values (itensities) of the surrounding pixels and sets the current pixel to the 1/8th value (average in a 3x3 grid)
    # - the bigger the grid, the more the blurring effect
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur:
    # - less blurring than the averaging operation
    # - each surrounding is given a weight
    # - weights are then averaged
    # - more natural than averaging
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur:
    # - similar algorithm like averaging but with median values
    # - more effective to reducing noise than the other two prior methods
    # - kernel size can be set to a single integer
    # - not meant for big kernel sizes like 7 or higher (generally)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral:
    # - most effective and used in advanced cv projects
    # - applies blurring but maintains the edges
    # - sigma space:
        # the larger the sigma space the further away pixels can influence the current pixel
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)