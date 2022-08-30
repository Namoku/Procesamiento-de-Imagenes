import cv2 as cv
import numpy as nm
import os

#Make an array of 120,000 bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpArray = nm.array(randomByteArray)

#Convert the array to make a 400x300 grayscale image
grayImage = flatNumpArray.reshape(300, 400)
cv.imwrite('RandomGray.png', grayImage)
cv.imshow('RandomGray.png', grayImage)
cv.waitKey()

#Convert the array to make a 400x100
bgrImage = flatNumpArray.reshape(100, 400, 3)
cv.imwrite('RandomColor.png', bgrImage)
cv.imshow('RandomColor.png', bgrImage)
cv.waitKey()
