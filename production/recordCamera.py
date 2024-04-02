from camera.cameraSettings import Camera
from time import time

class Record:
    def __init__(self) -> None:
        self.cam = Camera()
        self.cam.fps = 5

    def start(self, sec=30):
        startTime = time()
        while time()-startTime < sec:
            frame = self.cam.capture_array()
            self.cam.write(frame)
        self.cam.shutdown()

if __name__ == '__main__':
    rec = Record()
    rec.start()