import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera import Camera
from linesProcessing import LinesProcess
from motor import ControlMotor, Accueil

class Controller:
    def __init__(self) -> None:
        self.camera = Camera()
        self.accueilMotor = Accueil()
        self.finMotor = Accueil()
        self.controlMotor = ControlMotor()
        self.linesProcess = LinesProcess(self.camera.mid)

    def waiting(self) -> None:
        print('Waiting')
        while not self.camera.isRecording:
            self.camera.checkRecording()

    def start(self) -> None:
        print('Start')
        self.accueilMotor.start()
        self.camera.start()
        while self.camera.isRecording:
            coords = self.camera.detectLineInFrame(preview=False, saveOutput=False)
            line = self.linesProcess.output(coords)
            self.controlMotor.set(line)
            self.camera.checkRecording()
        self.camera.stop()
        self.finMotor.start()