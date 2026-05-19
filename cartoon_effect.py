import cv2

img = cv2.imread("Res/cartoon.png")
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur img
blur = cv2.medianBlur(g, 5)

#edge detection
edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Cartoon Effect", cartoon)
cv2.waitKey(0)

