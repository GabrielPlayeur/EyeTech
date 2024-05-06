import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent)
from detectLine import DetectLine
import cv2

<<<<<<< HEAD
cap = cv2.VideoCapture(f"{sys.argv[0]}.mp4")
=======
size = (800,400)
cap = cv2.VideoCapture(f"{sys.argv[1]}.mp4")
>>>>>>> d597cb7613b2f07aafe702f091424899196d3b3b
while(cap.isOpened()):
    _, frame = cap.read()
    d = DetectLine(frame)
    d.showImage(d.cropped_canny, "canny")
    d.showImage(d.lane_canny, "lane canny")
    d.showImage(d.getFinalImage(), "combo")
    print(d.lines, d.cropped_canny.shape)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()