from .parentsMotor import ParentsMotor, PWMOutputDevice

class ControlMotor(ParentsMotor):
    def __init__(self, vibG: PWMOutputDevice, vibD: PWMOutputDevice) -> None:
        self.MG = vibG
        self.MD = vibD

    def set(self, line: int) -> None:
        """Set the motors power to a specific value base on the line given"""
        if line == 0 :
            self.VIBD(0)
            self.VIBG(0)
        elif line == 1 :
            self.VIBD(0.33)
        elif line == 2 :
            self.VIBD(0.66)
        elif line == -1 :
            self.VIBG(0.33)
        elif line == -2 :
            self.VIBG(0.66)
        elif line == - 10 :
            self.VIBG(1)
        elif line == 10 :
            self.VIBD(1)