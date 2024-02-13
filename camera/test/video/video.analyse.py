import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
from detectLine import DetectLine
import cv2

cap = cv2.VideoCapture(f"{sys.argv[1]}.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    d = DetectLine(frame)
    d.showImage(cv2.resize(d.cropped_canny, (300, 500)), "canny")
    d.showImage(cv2.resize(d.lane_canny, (300, 500)), "lane canny")
    d.showImage(cv2.resize(d.getFinalImage(), (300, 500)), "combo")
    print(d.lines, d.cropped_canny.shape)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()