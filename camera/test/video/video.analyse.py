import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
from detectLine import DetectLine
import cv2

size = (800,400)
cap = cv2.VideoCapture(f"{sys.argv[1]}.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    d = DetectLine(frame)
    d.showImage(d.cropped_canny, "canny mid")
    d.showImage(d.region_of_interest(d.lane_canny, region="left"), "canny left")
    d.showImage(d.region_of_interest(d.lane_canny, region="right"), "canny right")
    d.showImage(d.lane_canny, "lane canny")
    d.showImage(d.getFinalImage(), "combo")
    print(d.lines, d.cropped_canny.shape)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()