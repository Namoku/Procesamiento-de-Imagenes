import cv2
import numpy as np

img = cv2.imread('sample.jpg')
num_rows, num_cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
cv2.imshow('Translation', img_rotation)
cv2.waitKey()