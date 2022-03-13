import cv2
from matplotlib import pyplot as plot

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)

plot.imshow(img)

plot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


