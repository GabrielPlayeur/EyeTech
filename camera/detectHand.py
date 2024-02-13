import cv2
import mediapipe as mp

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_untils

webcam=cv2.VideoCapture(0)
while webcam.isOpened():
    success, img = webcamred()

    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=mp_hands.Hands(max_num_hands=3,min_detection_confidence=0.7,min_tracking_confidence=0.7).process(img)
    
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    if results.multi_hands_landmarks:
        for hand_landmarks in results.multi_hands_landmarks:
            mp_drawing.draw_landmarks(img,hand_landmarks,connections=mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Koolac',img)
    if cv2.waitKey(5)and 0xFF ==ord("q"):
        break
webcam.release()
cv2.destroyAllWindows()

hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_hand.xml')
cap = cv2.VideoCapture(0)

while True:
    # Lire une image de la webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détecter les mains dans l'image
    hands = hand_cascade.detectMultiScale(gray, 1.1, 5)

    # Dessiner des rectangles autour des mains détectées
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Afficher l'image avec les rectangles dessinés
    cv2.imshow('Hand Detection', frame)

    # Sortir de la boucle si la touche 'q' est enfoncée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()