import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
from detectLine import DetectLine
import cv2

PATH_IMG = "../image/"

def test_imageTransf():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    d = DetectLine(frame)
    d.showImage(d.canny,"canny")
    cv2.waitKey(0)
    d.showImage(d.canny,"region_of_interest")
    cv2.waitKey(0)
    d.showFinalImage()
    cv2.waitKey(0)

def test_lines():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    d = DetectLine(frame)
    print(f"Lines: {d.lines}")

if __name__ == "__main__":
    test_imageTransf()
    test_lines()