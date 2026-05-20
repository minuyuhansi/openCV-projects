import cv2

eye_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

img = cv2.imread("Res/person.png")
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eyes = eye_detector.detectMultiScale(
    g,  
    scaleFactor=1.1,    
    minNeighbors=10
)

for (x, y, w, h) in eyes:

    center = (x + w // 2, y + h // 2)
    axes = (w // 2, h // 5)

    cv2.ellipse(img,center,axes,0,0,360,
        (0, 255, 0),2
    )

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)

