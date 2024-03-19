import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
import cv2
from detectBlackScreen import DetectBlackScreen

PATH_IMG = "../image/"

def test_canny():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    d = DetectBlackScreen(frame)
    d.showAllImage(0)

def test_counterWhitePixel():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    d = DetectBlackScreen(frame)
    print(d.countWhitePixel())

def test_isBlack():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    d = DetectBlackScreen(frame)
    print(d.isBlack())

if __name__ == "__main__":
    test_canny()
    test_counterWhitePixel()
    test_isBlack()