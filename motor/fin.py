from parentsMotor import ParentsMotor
from time import sleep

class fin (ParentsMotor) :
    def __init__(self) -> None:
        super().__init__()

    def long (self): 
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBG(1)
        sleep(3*self.duree)
        self.VIBG(0) 
        self.VIBG(0)

    def court (self):
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBG(1)
        sleep(self.duree)
        self.VIBG(0) 
        self.VIBG(0)

    def fin (self):
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
