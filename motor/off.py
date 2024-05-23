from .parentsMotor import ParentsMotor, PWMOutputDevice
from time import sleep

class Off(ParentsMotor):
    def __init__(self, vibG: PWMOutputDevice, vibD: PWMOutputDevice) -> None:
        self.MG = vibG
        self.MD = vibD
        self.duree = 0.25

    def start(self) -> None:
        """vibration du Off"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(2*self.duree)
        self.VIBG(0)
        self.VIBD(0)

        self.VIBG(0.66)
        self.VIBD(0.66)
        sleep(2*self.duree)
        self.VIBG(0)
        self.VIBD(0)
        sleep(self.duree)

        self.VIBG(0.33)
        self.VIBD(0.33)
        sleep(2*self.duree)
        self.VIBG(0)
        self.VIBD(0)

if __name__ == "__main__":
    p = ParentsMotor()
    p.setPin()
    Off(p.MG, p.MD).start()