import path
import sys
from time import time
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from camera import Camera
from time import time

class Record:
    def __init__(self) -> None:
        self.cam = Camera()
        self.cam.fps = 15

    def start(self, sec=10):
        print('-----------------GO------------------------')
        startTime = time()
        while time()-startTime < sec:
            frame = self.cam.capture_array()
            self.cam.write(frame)
        self.cam.shutdown()

if __name__ == '__main__':
    rec = Record()
    rec.start()