import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera.cameraSettings import Camera
from linesProcessing.main import LinesProcess

class Controller:
    def __init__(self) -> None:
        self.camera = Camera()
        self.linesProcess = LinesProcess(self.camera.mid)

    def start(self):
        self.camera.start()
        while self.camera.isRecording:
            coords = self.camera.detectLineInFrame(preview=False, saveOutput=False)
            pos = self.linesProcess.output(coords)
        self.camera.stop()