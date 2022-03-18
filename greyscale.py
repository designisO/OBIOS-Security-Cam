import numpy as np
import cv2


# selecting the webcam
cap = cv2.VideoCapture(0)

# Coninuous reading of the webcam.

while True:
    ret, frame = cap.read()  # reading frame by frame

    # displaying the frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Color', frame) #frame with color
    cv2.imshow('Gray', gray)    #frame in grayscale
    if cv2.waitKey(20) & 0xFF == ord('q'): # quiting application
        break