from picamera2 import Picamera2
from cv2 import VideoWriter, VideoWriter_fourcc, destroyAllWindows, waitKey
from .detectLine import DetectLine
from .detectBlackScreen import DetectBlackScreen
import numpy as np

class Camera(Picamera2):
    def __init__(self, size=(808,606), outputFileName="test.mp4") -> None:
        super().__init__()
        self.size = size
        self.mid = size[0]//2
        self.fps = 5
        self.config = {"format": 'XRGB8888', "size": self.size}
        self.configure(self.create_preview_configuration(main=self.config))
        self.writer = VideoWriter(outputFileName, VideoWriter_fourcc(*'mp4v'), self.fps, self.size, True)
        self.isRecording = False
        super().start()

    def detectLineInFrame(self, preview=False, saveOutput=False) -> list[list[int]]:
        """Return the position of 2 lines detect in the camera frame. This frame can be preview in a window or save in the chosen mp4 file."""
        frame = self.capture_array()
        detectLine = DetectLine(frame)
        if saveOutput:
            self.write(detectLine.getFinalImage())
        if preview:
            self.preview(detectLine)
        return detectLine.lines

    def checkStopRecordingCondition(self) -> None:
        """Checks to update the camera status if the camera frame is seen as a black screen."""
        frame = self.capture_array()
        self.isRecording = not DetectBlackScreen(frame).isBlack()

    def isBlack(self) -> bool:
        """Return if the camera frame is seen as a black screen."""
        frame = self.capture_array()
        return DetectBlackScreen(frame).isBlack()

    def write(self, frame: np.ndarray) -> None:
        """Write the frame in the choosen output mp4 file."""
        self.writer.write(frame[:,:,0:3])

    def preview(self, detectLine: DetectLine, ms=1) -> None:
        """Create a visual window to be able to watch the frame during ms time."""
        detectLine.showFinalImage()
        self.wait(ms)

    def start(self) -> None:
        """Set the status of the camera to recording."""
        self.isRecording = True

    def stop(self) -> None:
        """Stop the camera wrinting and close all the visual window."""
        self.isRecording = False
        self.writer.release()
        destroyAllWindows()

    def shutdown(self) -> None:
        """Stop the camera recording and writing and close all the visual window."""
        self.stop()
        super().stop()

    def wait(self, ms, exitKey='q') -> None:
        """Wait the time in ms second to slow tthe display (for freeze ms=0). If the exit key is press in this interval the recording stop."""
        if waitKey(ms) & 0xFF == ord(exitKey):
            self.isRecording = False