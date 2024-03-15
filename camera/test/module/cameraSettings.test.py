import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
from cameraSettings import Camera
from detectLine import DetectLine

PATH_IMG = "../image/"

def test_record():
    c = Camera()
    c.checkStopRecordingCondition()
    print(f"isRecording: {c.isRecording}")
    c.start()
    print(f"isRecording: {c.isRecording}")
    c.preview(DetectLine(c.capture_array()),ms=0)
    print("Try writing video file...")
    c.write(c.capture_array())
    print("File record!")
    print("Waiting black screen...")
    while not c.isBlack():
        pass
    print("Black screen detect!")
    c.stop()
    print(f"isRecording: {c.isRecording}")

def test_lineDetection():
    c = Camera()
    line = c.detectLineInFrame(preview=True)
    print(f"line : {line}")

if __name__ == "__main__":
    test_record()
    test_lineDetection()