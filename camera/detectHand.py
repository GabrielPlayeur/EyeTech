import cv2
from cameraSettings import Camera

hand_cascade = cv2.CascadeClassifier('palm.xml')
cam = Camera()
<<<<<<< HEAD
=======
cam.start()
print("start")
>>>>>>> 08c84fa864ea89692fab971ab990a36f4c5efed4

while True:
    # Lire une image de la webcam
    frame = cam.capture_array()
<<<<<<< HEAD
    # Détecter les mains dans l'image    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5) #All detected hands get put into an array
    print(len(hands))

# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()
=======
    # Détecter les mains dans l'image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5) #All detected hands get put into an array
    print(len(hands))
    cv2.imshow("test",gray)
cam.stop()
>>>>>>> 08c84fa864ea89692fab971ab990a36f4c5efed4
