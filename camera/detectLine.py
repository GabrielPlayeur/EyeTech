import cv2
import numpy as np
from warnings import simplefilter
simplefilter('ignore', np.RankWarning)

class DetectLine:
    def __init__(self, frame: np.ndarray) -> None:
        self.image = frame
        self.lane_image = np.copy(self.image)
        self.lane_canny = self.canny(self.lane_image) #Search every line with gradiant
        self.cropped_canny = self.region_of_interest(self.lane_canny) #Croppe image
        self.lines =  self.get_lines(self.cropped_canny) #Find lines

    def get_lines(self, image: np.ndarray) -> dict[list[int]]:
        """Get the position of 2 lines detect on the camera. {'left': [x1, y1, x2, y2], 'right': [x1, y1, x2, y2]}"""
        lines = cv2.HoughLinesP(image, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
        return self.average_slope_intercept(lines)

    def make_points(self, line: np.ndarray) -> list[int]:
        if not isinstance(line, np.ndarray):
            return [[300, self.image.shape[0], 300, self.image.shape[0]]]
        slope, intercept = line
        if  -0.01 <= slope <= 0.01:
            return [[0, 0, 10, 10]]
        y1 = int(self.image.shape[0])
        y2 = int(y1*3/5)
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return [x1, y1, x2, y2]

    def average_slope_intercept(self, lines: np.ndarray) -> dict[list[int]]:
        left_fit = []
        right_fit = []
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
        left_line  = self.make_points(left_fit_average)
        right_line = self.make_points(right_fit_average)
        averaged_lines = {"left": left_line, "right": right_line}
        return averaged_lines

    def canny(self, image: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        canny = cv2.Canny(gray, 50, 150)
        return canny

    def display_lines(self, image: np.ndarray, lines: dict[list[int]]) -> np.ndarray:
        line_image = np.zeros_like(image)
        if lines is not None:
            for x1, y1, x2, y2 in lines.values():
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
        return line_image

    def region_of_interest(self, canny: np.ndarray) -> np.ndarray:
        height = canny.shape[0]
        width = canny.shape[1]
        mask = np.zeros_like(canny)
        triangle = np.array([[
        (0, height),
        (width//2, height//2),
        (width, height),]], np.int32)
        cv2.fillPoly(mask, triangle, 255)
        masked_image = cv2.bitwise_and(canny, mask)
        return masked_image

    def getFinalImage(self) -> np.ndarray:
        line_image = self.display_lines(self.lane_image, self.lines)
        combo_image = cv2.addWeighted(self.image, 0.8, line_image, 1, 0)
        return combo_image

    def showImage(self, image: np.ndarray, title: str) -> None:
        cv2.imshow(title, image)

    def showFinalImage(self) -> None:
        self.showImage(self.getFinalImage(), "result")