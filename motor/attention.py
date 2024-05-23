from .parentsMotor import ParentsMotor, PWMOutputDevice
from time import sleep

class Attention(ParentsMotor):
    def __init__(self, vibG: PWMOutputDevice, vibD: PWMOutputDevice) -> None:
        self.MG = vibG
        self.MD = vibD
        self.duree = 0.25

    def start(self) -> None:
        """vibration du attention"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(0.5*self.duree)
        self.VIBG(0)
        self.VIBD(0)
        sleep(0.5*self.duree)
        self.VIBG(1)
        self.VIBD(1)
        sleep(0.5*self.duree)
        self.VIBG(0)
        self.VIBD(0)
        sleep(0.5*self.duree)
        self.VIBG(1)
        self.VIBD(1)
        sleep(0.5*self.duree)

if __name__ == "__main__":
    p = ParentsMotor()
    p.setPin()
    Attention(p.MG, p.MD).start()