import cv2
import numpy as np

img = cv2.imread("Res/colors.png")
# convert BGR tO HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# red color rangein HSV 
lower_red = np.array([0, 120, 80])  
upper_red = np.array([10, 255, 255])

# create a mask
mask = cv2.inRange(hsv,lower_red,upper_red)

result = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Original Image", img)
cv2.imshow("Mask", result)

cv2.waitKey(0)

