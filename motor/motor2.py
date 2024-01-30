from gpiozero import DigitalOutputDevice
from time import sleep

PWM1 = PWMOutputDevice(33)

PWM1.value = 0.5
sleep(2)