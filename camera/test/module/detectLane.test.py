import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
from detectLine import DetectLine
import cv2

PATH_IMG = "../image/"

def test_imageTransfMid():
    frame = cv2.imread(PATH_IMG+"test_img_mid.jpg")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showFinalImage()
    cv2.waitKey(0)

def test_imageTransfLeft():
    frame = cv2.imread(PATH_IMG+"test_img_left.jpg")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showImage(d.region_of_interest(d.lane_canny, region="left"), "crop left")
    d.showFinalImage()
    cv2.waitKey(0)

def test_imageTransfRight():
    frame = cv2.imread(PATH_IMG+"test_img_right.jpg")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showImage(d.region_of_interest(d.lane_canny, region="right"), "crop right")
    d.showFinalImage()
    cv2.waitKey(0)

def test_imageTransfTurn():
    frame = cv2.imread(PATH_IMG+"test_img_turn.jpg")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showImage(d.region_of_interest(d.lane_canny, region="right"), "crop right")
    d.showFinalImage()
    cv2.waitKey(0)

def test_image1():
    frame = cv2.imread(PATH_IMG+"image_1.png")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showImage(d.region_of_interest(d.lane_canny, region="right"), "crop right")
    d.showFinalImage()
    cv2.waitKey(0)

def test_image2():
    frame = cv2.imread(PATH_IMG+"image_2.jpg")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showImage(d.region_of_interest(d.lane_canny, region="right"), "crop right")
    d.showFinalImage()
    cv2.waitKey(0)

def test_image3():
    frame = cv2.imread(PATH_IMG+"image3.png")
    d = DetectLine(frame)
    d.showImage(d.lane_canny,"canny")
    d.showImage(d.cropped_canny,"region_of_interest")
    d.showImage(d.region_of_interest(d.lane_canny, region="right"), "crop right")
    d.showFinalImage()
    cv2.waitKey(0)

def test_lines():
    frame = cv2.imread(PATH_IMG+"test_img_mid.jpg")
    d = DetectLine(frame)
    print(f"Lines: {d.lines}")

def test_linePos():
    frame = cv2.imread(PATH_IMG+"test_img_mid.jpg")
    l = DetectLine(frame).findLinePos([78, 606, 249, 363])
    r = DetectLine(frame).findLinePos([560, 606, 489, 363])
    print(l, r)
    assert l == "left"
    assert r == "right"

if __name__ == "__main__":
    test_imageTransfMid()
    test_imageTransfLeft()
    test_imageTransfRight()
    test_imageTransfTurn()
    test_image1()
    test_image2()
    test_image3()
    test_lines()
    test_linePos()