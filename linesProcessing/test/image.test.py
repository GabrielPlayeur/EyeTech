import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent+"\\camera")
sys.path.append(directory.parent.parent.parent+"\\linesProcessing")
from detectLine import DetectLine
from lineProcess import LinesProcess
import cv2

PATH_IMG = "../image/"

def test_imageTransfMid():
    frame = cv2.imread(PATH_IMG+"test_img_mid.jpg")
    d = DetectLine(frame)
    o = LinesProcess().output(d.get_pos())
    print(o)
    d.showFinalImage()
    cv2.waitKey(0)

def test_imageTransfLeft():
    frame = cv2.imread(PATH_IMG+"test_img_left.jpg")
    d = DetectLine(frame)
    o = LinesProcess().output(d.get_pos())
    print(o)
    d.showFinalImage()
    cv2.waitKey(0)

def test_imageTransfRight():
    frame = cv2.imread(PATH_IMG+"test_img_right.jpg")
    d = DetectLine(frame)
    o = LinesProcess().output(d.get_pos())
    print(o)
    d.showFinalImage()
    cv2.waitKey(0)

def test_imageTransfTurn():
    frame = cv2.imread(PATH_IMG+"test_img_turn.jpg")
    d = DetectLine(frame)
    o = LinesProcess().output(d.get_pos())
    print(o)
    d.showFinalImage()
    cv2.waitKey(0)

if __name__ == "__main__":
    test_imageTransfMid()
    test_imageTransfLeft()
    test_imageTransfRight()
    test_imageTransfTurn()