import cv2
from cameraSettings import Camera

hand_cascade = cv2.CascadeClassifier('palm.xml')
cam = Camera()
cam.start()
print("start")

while True:
    # Lire une image de la webcam
    frame = cam.capture_array()
    # Détecter les mains dans l'image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5) #All detected hands get put into an array
    print(len(hands))
    cv2.imshow("test",gray)
cam.stop()