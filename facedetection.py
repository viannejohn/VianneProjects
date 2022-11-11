import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade=cv2.CascadeClassifier('haarcascade_mcs_nose.xml');
#mouth_cascade=cv2.CascadeClassifier('haarcascade_mcs_mouth.xml');

cap = cv2.VideoCapture(0)

while True:
    _, img  = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
    nose = nose_cascade.detectMultiScale(gray, 1.1, 4)
    #mouth = mouth_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=4)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #for (x, y, w, h) in mouth:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
    for (x, y, w, h) in nose:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()