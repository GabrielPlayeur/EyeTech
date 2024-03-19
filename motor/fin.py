from .parentsMotor import ParentsMotor, PWMOutputDevice
from time import sleep

class Fin(ParentsMotor):
    def __init__(self, vibG: PWMOutputDevice, vibD: PWMOutputDevice) -> None:
        self.MG = vibG
        self.MD = vibD
        self.duree = 0.25

    def long(self) -> None:
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(3*self.duree)
        self.VIBG(0) 
        self.VIBD(0)

    def court(self) -> None:
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(self.duree)
        self.VIBG(0) 
        self.VIBD(0)

    def start(self) -> None:
        """fin en morse"""
        self.court()
        self.court()
        self.long()
        self.court()
        sleep(3*self.duree)
        self.court()
        self.court()
        sleep(3*self.duree)
        self.long()
        self.court()

if __name__ == "__main__":
    Fin().start()