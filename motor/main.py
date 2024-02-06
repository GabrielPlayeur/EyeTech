from parentsMotor import ParentsMotor

class Control (ParentsMotor) :
    def __init__(self) -> None:
        super().__init__()

    def controlmoteur (self, puissance):

        if puissance == 0 :
            self.VIBD(0)
            self.VIBG(0)

        elif puissance == 1 :
            self.VIBD(0.5)

        elif puissance == 2 :
            self.VIBD(1)

        elif puissance == -1 :
            self.VIBG(0.5)

        elif puissance == -2 :
            self.VIBG(1)
