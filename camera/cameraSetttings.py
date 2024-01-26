from picamera2 import Picamera2
from cv2 import VideoWriter, VideoWriter_fourcc, destroyAllWindows, waitKey
from detectLine import DetectLine

class Camera(Picamera2):
    def __init__(self, size=(808,606), outputFileName="test.mp4") -> None:
        self.size = size
        self.fps = 5
        self.config = {"format": 'XRGB8888', "size": self.size}
        self.configure(self.create_preview_configuration(main=self.config))
        self.writer = VideoWriter(outputFileName, VideoWriter_fourcc(*'mp4v'), self.fps, self.size, True)
        self.isRecording = False

    def detectLineInFrame(self, preview=False, saveOutput=False) -> list[list[int]]:
        frame = self.capture_array()
        detectLine = DetectLine(frame)
        if saveOutput:
            self.write(detectLine.getFinalImage())
        if preview:
            detectLine.showFinalImage()
        return detectLine.lines

    def write(self, frame) -> None:
        self.writer.write(frame[:,:,0:3])

    def start(self) -> None:
        self.isRecording = True
        super().start()

    def stop(self) -> None:
        self.writer.release()
        destroyAllWindows()
        super().stop()

    def wait(self, exitKey='q', ms=1) -> None:
        if waitKey(ms) & 0xFF == ord(exitKey):
            self.isRecording = False