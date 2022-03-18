import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

# classifiers for face & body
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

recording = True

# Setting frame size and video format for recording
frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"MP4V")
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # greyscale camera
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Accuracy of detection
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        recording = True

    # rectangle around faces
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3) # create blue rectangle (BGR)


    cv2.imshow("OBIOS Security Camera", frame)

    if cv2.waitKey(1) == ord('q'): # quit app
        break

out.release()
cap.release()
cv2.destroyAllWindows()