import cv2
import numpy as np

img = cv2.imread("Res/person.png")
g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold mask
_, mask = cv2.threshold(g, 210, 255, cv2.THRESH_BINARY_INV)
#remove background
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Background Removal", result)
cv2.waitKey(0)
