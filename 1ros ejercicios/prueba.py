import cv2

img = cv2.imread('sample.jpg')
print(img.shape)
print(img.size)
print(type(img))
print(img)
cv2.imshow('Gatito', img)
cv2.waitKey()
