import cv2
import numpy as np
from picamera2 import Picamera2

class DetectLine:
    def __init__(self, frame):
        self.image = frame
        self.lane_image = np.copy(self.image)
        self.lane_canny = self.canny(self.lane_image)
        self.cropped_canny = self.region_of_interest(self.lane_canny)
        self.averaged_lines =  self.get_lines(self.cropped_canny)
        self.line_image = self.display_lines(self.lane_image, self.averaged_lines)
        self.combo_image = cv2.addWeighted(self.image, 0.8, self.line_image, 1, 0)

    def get_lines(self, image):
        lines = cv2.HoughLinesP(image, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
        averaged_lines = self.average_slope_intercept(self.image, lines)
        return averaged_lines

    def make_points(self, image, line: np.ndarray):
        if not isinstance(line, np.ndarray):
            return [[300, image.shape[0], 300, image.shape[0]]]
        slope, intercept = line
        if  -0.01 <= slope <= 0.01:
            return [[0, 0, 10, 10]]

        y1 = int(image.shape[0])
        y2 = int(y1*3/5)
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return [[x1, y1, x2, y2]]

    def average_slope_intercept(self, image, lines):
        left_fit    = []
        right_fit   = []
        if lines is None:
            return None
        for line in lines:
            for x1, y1, x2, y2 in line:
                fit = np.polyfit((x1,x2), (y1,y2), 1)
                slope = fit[0]
                intercept = fit[1]
                if slope < 0:
                    left_fit.append((slope, intercept))
                else:
                    right_fit.append((slope, intercept))

        left_fit_average  = np.average(left_fit, axis=0)
        right_fit_average = np.average(right_fit, axis=0)
        left_line  = self.make_points(image, left_fit_average)
        right_line = self.make_points(image, right_fit_average)
        averaged_lines = [left_line, right_line]
        return averaged_lines

    def canny(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        kernel = 5
        blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
        canny = cv2.Canny(gray, 50, 150)
        return canny

    def display_lines(self, img, lines):
        line_image = np.zeros_like(img)
        if lines is not None:
            for line in lines:
                for x1, y1, x2, y2 in line:
                    cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
        return line_image

    def region_of_interest(self, canny):
        height = canny.shape[0]
        width = canny.shape[1]
        mask = np.zeros_like(canny)

        triangle = np.array([[
        (0, height),
        (400, 300),
        (height, height),]], np.int32)

        cv2.fillPoly(mask, triangle, 255)
        masked_image = cv2.bitwise_and(canny, mask)
        return masked_image

    def show(self, image, title="result"):
        cv2.imshow(title, image)

    def showRes(self):
        self.show(self.combo_image)

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (808, 606)}))
picam2.start()

while True:
    im = picam2.capture_array()
    detectLine = DetectLine(im)

    detectLine.showRes()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break