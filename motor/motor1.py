import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)   ##je prefere la numerotation BOARD plutot que BCM

Moteur1A = 16      ## premiere entrée du premier moteur, pin 16
Moteur1B = 18      ## deuxieme entrée du premier moteur, pin 18
Moteur1E = 22      ## enable du premier moteur, pin 22

GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois broches du Raspberry Pi sont des sorties
GPIO.setup(Moteur1B,GPIO.OUT)
GPIO.setup(Moteur1E,GPIO.OUT)

pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la broche 22 a une frequence de 50 Hz
pwm.start(100)   ## on commemnce avec un rapport cyclique de 100%


print ("Rotation sens direct, vitesse maximale (rapport cyclique 100%)")
GPIO.output(Moteur1A,GPIO.HIGH)
GPIO.output(Moteur1B,GPIO.LOW)
GPIO.output(Moteur1E,GPIO.HIGH)

sleep(5)  ## on laisse tourner le moteur 5 secondes avec des parametres

pwm.ChangeDutyCycle(40)  ## modification du rapport cyclique a 40%

print ("Rotation sens direct, au ralenti (rapport cyclique 40%)")

sleep(5)

print ("Rotation sens inverse, au ralenti (rapport cyclique 40%)")
GPIO.output(Moteur1A,GPIO.LOW)
GPIO.output(Moteur1B,GPIO.HIGH)

sleep(5)

pwm.ChangeDutyCycle(100)
print ("Rotation sens inverse, vitesse maximale (rapport cyclique 100%)")
sleep(5)

print ("Arret du moteur")
GPIO.output(Moteur1E,GPIO.LOW)

pwm.stop()    ## interruption du pwm

GPIO.cleanup()