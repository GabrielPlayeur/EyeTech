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
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showFinalImage()
    cv2.waitKey(0)

def test_lines():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    d = DetectLine(frame)
    print(f"Lines: {d.lines}")

def test_linePos():
    frame = cv2.imread(PATH_IMG+"test_image.jpg")
    l = DetectLine(frame).findLinePos([78, 606, 249, 363])
    r = DetectLine(frame).findLinePos([560, 606, 489, 363])
    print(l, r)
    assert l == "left"
    assert r == "right"

if __name__ == "__main__":
    test_imageTransf()
    test_lines()
    test_linePos()