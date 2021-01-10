import cv2

face_cascade = cv2.CascadeClassifier("/Users/parvnarang/Desktop/images/frontal_face.xml")

cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print("Could not open video device:")

while True:
    ret, img = cap.read()
    if ret == False:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('img', img)

    key = cv2.waitKey(5)

    if key == ord('q'):
        break

cap.release()