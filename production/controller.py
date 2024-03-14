import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera.cameraSettings import Camera
from motor.accueil import Accueil
from multiProcess import MultiProcess

class Controller:
    def __init__(self) -> None:
        self.camera = Camera()
        self.multiProcess = MultiProcess(self.camera)
        self.accueilMotor = Accueil()
        self.finMotor = Accueil()

    def waiting(self) -> None:
        while not self.camera.isRecording:
            self.camera.checkRecording()

    def start(self) -> None:
        self.accueilMotor.start()
        self.camera.start()
        self.multiProcess.start()
        self.camera.stop()
        self.finMotor.start()