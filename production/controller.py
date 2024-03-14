import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera.cameraSettings import Camera
from linesProcessing.main import LinesProcess
from motor.control import ControlMotor
from motor.accueil import Accueil

class Controller:
    def __init__(self) -> None:
        self.camera = Camera()
        self.accueilMotor = Accueil()
        self.finMotor = Accueil()
        self.controlMotor = ControlMotor()
        self.linesProcess = LinesProcess(self.camera.mid)

    def waiting(self) -> None:
        while not self.camera.isRecording:
            self.camera.checkRecording()

    def start(self) -> None:
        self.accueilMotor.start()
        self.camera.start()
        while self.camera.isRecording:
            coords = self.camera.detectLineInFrame(preview=False, saveOutput=False)
            line = self.linesProcess.output(coords)
            self.controlMotor.set(line)
            self.camera.checkRecording()
        self.camera.stop()
        self.finMotor.start()