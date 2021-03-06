
import numpy as np
import cv2 as cv

img = cv.imread('opencv-logo.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgGray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print("Number of contours = " + str(len(contours)))

cv.drawContours(img, contours, -1, (0, 255, 0), 3)

cv.imshow('Image', img)
cv.imshow('Image GRAY', imgGray)
cv.waitKey(0)
cv.destroyAllWindows()
