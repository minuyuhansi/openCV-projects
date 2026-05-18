import cv2

smile_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

img = cv2.imread("Res/smile.png")
g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

smiles = smile_detector.detectMultiScale(
    g,
    scaleFactor=1.8,
    minNeighbors=35
)

# Draw rectangles around smiles
for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

# Show image
cv2.imshow("Smile Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()