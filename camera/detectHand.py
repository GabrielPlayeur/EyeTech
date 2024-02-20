import cv2

hand_cascade = cv2.CascadeClassifier('palm.xml')
cap = cv2.VideoCapture(0)

while True:
    # Lire une image de la webcam
    _, frame = cap.read()
    # Détecter les mains dans l'image    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5) #All detected hands get put into an array
    hands = hand_cascade.detectMultiScale( 1.1, 5)


# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()