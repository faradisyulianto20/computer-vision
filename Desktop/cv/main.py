import cv2

img = cv2.imread('image.jpg', 0)
img = cv2.resize(img, (600, 600))

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()