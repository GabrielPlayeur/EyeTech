import cv2
import mediapipe as mp

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_untils

webcam=cv2.VideoCapture(0)
while webcam.isOpened():
    _, frame = webcam.red()

    results=mp_hands.Hands(max_num_hands=3,min_detection_confidence=0.7,min_tracking_confidence=0.7).process(frame)
   
webcam.release()
cv2.destroyAllWindows()

hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_hand.xml')
cap = cv2.VideoCapture(0)

while True:
    # Lire une image de la webcam
    _, frame = cap.read()
    # Détecter les mains dans l'image
    hands = hand_cascade.detectMultiScale( 1.1, 5)


# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()