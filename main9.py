import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)

cv.waitKey(0)
cv.destroyAllWindows()
