import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent+"\\camera")
sys.path.append(directory.parent.parent.parent+"\\linesProcessing")
from detectLine import DetectLine
from lineProcess import LinesProcess
import cv2

PATH_IMG = "../image/"
PATH_VIDEO = "../video/"
c=0

lp = LinesProcess()
size = (800,400)
cap = cv2.VideoCapture(f"{PATH_VIDEO+sys.argv[1]}.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    d = DetectLine(frame)
    o = lp.output(d.get_pos())
    print(o)
    d.showFinalImage()
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()