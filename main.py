import cv2

# second parameter is a flag which specifies the way images should be read
# 1, loads a color image
# 0, loads image in grayscale mode
# -1, loads image as such including alpha channel
img = cv2.imread('lena.jpg', -1)

print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()


