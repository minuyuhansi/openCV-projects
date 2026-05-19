import cv2

img = cv2.imread("Res/sketch.png")
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#invert img
invert = 255 - g

#blur img
blur = cv2.GaussianBlur(invert, (21, 21), 0)
inverted_blur = 255-blur

#create pencil sketch
sketch = cv2.divide(g, inverted_blur, scale=256.0)

cv2.imshow("Pencil Sketch", sketch)
cv2.waitKey(0)