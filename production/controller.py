import path
import sys
import os
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera import Camera
from linesProcessing import LinesProcess
from motor import ControlMotor, Accueil, Fin, ParentsMotor

class Controller:
    def __init__(self) -> None:
        self.camera = Camera()
        self.parentMotor = ParentsMotor()
        self.parentMotor.setPin()
        self.accueilMotor = Accueil(self.parentMotor.MG,self.parentMotor.MD)
        self.finMotor = Fin(self.parentMotor.MG,self.parentMotor.MD)
        self.controlMotor = ControlMotor(self.parentMotor.MG,self.parentMotor.MD)
        self.linesProcess = LinesProcess(self.camera.mid)

    def waiting(self) -> None:
        """Looping until the camera frame is cover to be seen as a black screen"""
        print('Waiting')
        while not self.camera.isBlack():
            pass

    def start(self) -> None:
        """Start the process to detect the lines and transmit the value to the motors until the camera is cover to create a black screen"""
        print('Start')
        self.accueilMotor.start()
        self.camera.start()
        while self.camera.isRecording:
            coords = self.camera.detectLineInFrame(preview=False, saveOutput=False)
            line = self.linesProcess.output(coords)
            self.controlMotor.set(line)
            self.camera.checkStopRecordingCondition()
        self.camera.stop()
        self.finMotor.start()
        print('Stop')

    def shutdown(self) -> None:
        """Shutdown the raspberry to prepare it for disconnection"""
        self.camera.shutdown()
        os.system('sudo halt')