from .parentsMotor import ParentsMotor, PWMOutputDevice
from time import sleep

class Battery(ParentsMotor):
    def __init__(self) -> None:
        super().__init__()
        self.condEnd = 0
    def getVoltage (self):
        sensorValue = ##le nom du pin qu'on utilise
        voltageValue = sensorValue * (3.3 / 65535) ##Conversion de la valeur en volt
        return (voltageValue)
    
   
    def endOfTime (self):
        if self.getVoltage() <= 3.4 and self.getVoltage() >= 3.3 and self.condEnd ==1:
            self.VIBG(1)
            self.VIBD(1)
            sleep(2)
            self.VIBG(0) 
            self.VIBD(0)
            self.condEnd = 0
        return None
    while True :
        endOfTime()
        sleep(1)
