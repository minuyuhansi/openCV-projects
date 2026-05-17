import cv2

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

img = cv2.imread("Res/blurFace.png")
g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_detector.detectMultiScale(
    g,
    scaleFactor=1.1,
    minNeighbors=5
)

# blur each faces
for (x, y, w, h) in faces:

    face = img[y:y+h, x:x+w]

    # apply blur
    # only odd number to add as kernel size
    blur = cv2.GaussianBlur(face, (15, 15), 0)

    # replace original face with blurred face
    img[y:y+h, x:x+w] = blur

cv2.imshow("Face Blur",img)
cv2.waitKey(0)

