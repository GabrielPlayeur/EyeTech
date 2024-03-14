import multiprocessing as mp
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera.cameraSettings import Camera
from linesProcessing.main import LinesProcess
from motor.control import ControlMotor

class MultiProcess:
    def __init__(self, camera: Camera) -> None:
        self.camera = camera
        self.controlMotor = ControlMotor()
        self.linesProcess = LinesProcess(self.camera.mid)

    def run(self):
        coords = self.camera.detectLineInFrame(preview=False, saveOutput=False)
        line = self.linesProcess.output(coords)
        self.controlMotor.set(line)
        self.camera.checkRecording()

    def start(self) -> None:
        with mp.Pool(processes=mp.cpu_count()) as pool:
            while self.camera.isRecording:
                pool.apply_async(self.run)