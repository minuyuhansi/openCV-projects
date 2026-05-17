import cv2

body_director = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_fullbody.xml')

img = cv2.imread("Res/fullBody.png")
g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bodies = body_director.detectMultiScale(
    g,
    scaleFactor=1.05,
    minNeighbors=5
)

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("Full Body Detection",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
