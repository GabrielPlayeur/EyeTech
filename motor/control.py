from parentsMotor import ParentsMotor

class ControlMotor(ParentsMotor) :
    def __init__(self) -> None:
        super().__init__()

    def set(self, line: int) -> None:
        if line == 0 :
            self.VIBD(0)
            self.VIBG(0)

        elif line == 1 :
            self.VIBD(0.5)

        elif line == 2 :
            self.VIBD(1)

        elif line == -1 :
            self.VIBG(0.5)

        elif line == -2 :
            self.VIBG(1)