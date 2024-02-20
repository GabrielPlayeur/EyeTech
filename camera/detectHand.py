import cv2
from cameraSettings import Camera

hand_cascade = cv2.CascadeClassifier('palm.xml')
cam = Camera()

while True:
    # Lire une image de la webcam
    frame = cam.capture_array()
    # Détecter les mains dans l'image    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5) #All detected hands get put into an array
    print(len(hands))

# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()