import cv2 as cv

img = cv.imread('sample.jpg')
img2 = 'sample.jpg'
gray_image = cv.imread(img2,cv.IMREAD_GRAYSCALE)
img_small = cv.resize(img, (0,0), fx=0.5, fy=0.5)
cv.imshow('Perrito corriendo',img)
cv.imshow('Perrito corriendo en gris',gray_image)
cv.imshow('Perrito corriendo chiquito',img_small)
#cv.imwrite('sample_gray.jpg',gray_image)
cv.waitKey()