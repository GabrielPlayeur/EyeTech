import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera.cameraSettings import Camera

class Controller:
    def __init__(self) -> None:
        self.camera = Camera()

    def start(self):
        self.camera.start()
        while self.camera.isRecording:
            self.camera.detectLineInFrame(preview=False, saveOutput=False)
        self.camera.stop()