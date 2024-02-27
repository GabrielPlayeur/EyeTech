from gpiozero import PWMOutputDevice

class ParentsMotor :
    def __init__(self) -> None:
        self.MG = PWMOutputDevice("GPIO13")
        self.MD = PWMOutputDevice("GPIO19")

    def VIBG (self,value):
        """vibration moteur gauche"""
        self.MG.value = value

    def VIBD (self,value):
        """vibration moteur droit"""
        self.MD.value = value