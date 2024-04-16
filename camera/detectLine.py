import cv2
import numpy as np
from warnings import simplefilter
simplefilter('ignore', np.RankWarning)

class DetectLine:
    def __init__(self, frame: np.ndarray) -> None:
        self.image = frame
        self.lane_image = np.copy(self.image)
        self.lane_canny = self.canny(self.lane_image) #Search every line with gradiant
        self.cropped_canny = self.region_of_interest(self.lane_canny, region="mid") #Croppe image
        self.lines =  self.get_lines(self.cropped_canny) #Find lines

    def get_lines(self, image: np.ndarray) -> dict[list[int]]:
        """Get the position of 2 lines detect on the camera. {'left': [x1, y1, x2, y2], 'right': [x1, y1, x2, y2]}"""
        lines = cv2.HoughLinesP(image, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
        linesAverage = self.average_slope_intercept(lines)
        fixLines = self.fixLineMissing(self.lane_canny, linesAverage)
        return fixLines

    def make_points(self, line: np.ndarray) -> list[int]:
        """Return the position of a line given by a equation. [x1, y1, x2, y2]"""
        if not isinstance(line, np.ndarray):
            return [300, self.image.shape[0], 300, self.image.shape[0]]
        slope, intercept = line
        if  -0.01 <= slope <= 0.01:
            return [0, 0, 10, 10]
        y1 = int(self.image.shape[0])
        y2 = int(y1*3/5)
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return [x1, y1, x2, y2]

    def findLinePos(self, line: np.ndarray) -> str:
        """Return if given line is the right or the left one"""
        if line==[0,0,10,10] or line==[300, 606, 300, 606]:
            return "none"
        return "left" if line[0]<line[2] else "right"

    def average_slope_intercept(self, lines: np.ndarray) -> dict[list[int]]:
        """Return the average of all the found lines to return only 2 lines. {'left': [x1, y1, x2, y2], 'right': [x1, y1, x2, y2]}"""
        first_fit = []
        second_fit = []
        if lines is None:
            return {"left": [0,0,0,0], "right": [800,800,800,800]}
        for line in lines:
            for x1, y1, x2, y2 in line:
                fit = np.polyfit((x1,x2), (y1,y2), 1)
                slope = fit[0]
                intercept = fit[1]
                if slope < 0:
                    first_fit.append((slope, intercept))
                else:
                    second_fit.append((slope, intercept))
        first_fit_average  = np.average(first_fit, axis=0)
        second_fit_average = np.average(second_fit, axis=0)
        first_line  = self.make_points(first_fit_average)
        second_line = self.make_points(second_fit_average)
        first_key = self.findLinePos(first_line)
        second_key = self.findLinePos(second_line)
        averaged_lines = {first_key: first_line, second_key: second_line}
        return averaged_lines

    def fixLineMissing(self, canny: np.ndarray,  averaged_lines: dict) -> dict[list[int]]:
        """Try to identify lane in the side where nothing got find by using an other region of interest"""
        if not "none" in averaged_lines.keys(): #No missing lines
            return averaged_lines
        if averaged_lines.get("right"): #Missing left line
            key = 'left'
        elif averaged_lines.get('left'): #Missing right line
            key = "right"
        else: #Missing both line
            return {"left":[0,0,10,10], "right":[0,0,10,10]}
        cropped = self.region_of_interest(canny, region=key)
        lines = cv2.HoughLinesP(cropped, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
        fixLines = self.average_slope_intercept(lines)
        if  ["none","none"] ==  list(fixLines.keys()): #no newline find
            return  averaged_lines
        averaged_lines[key] =  fixLines['right'] if fixLines.get("right") else fixLines['left']
        del averaged_lines['none']
        return averaged_lines

    def canny(self, image: np.ndarray) -> np.ndarray:
        """return the frame with a gradian apply"""
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        canny = cv2.Canny(gray, 50, 75)
        return canny

    def display_lines(self, image: np.ndarray, lines: dict[list[int]]) -> np.ndarray:
        """Return the 2 found lines in a image type"""
        line_image = np.zeros_like(image)
        if lines is not None:
            for x1, y1, x2, y2 in lines.values():
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
        return line_image

    def region_of_interest(self, canny: np.ndarray, region: str) -> np.ndarray:
        """Crop the frame to return only the desired region. The shape is similare to a triangle."""
        mask = np.zeros_like(canny)
        triangle = self.selectRegionShape(canny, region)
        cv2.fillPoly(mask, triangle, 255)
        masked_image = cv2.bitwise_and(canny, mask)
        return masked_image

    def selectRegionShape(self, canny: np.ndarray, region: str) -> np.array:
        """Return the select shape base on the region name"""
        height = canny.shape[0]
        width = canny.shape[1]
        match region:
            case "left":
                triangle = np.array([[
                (0, height),
                (0, height//2),
                (width//2, height),]], np.int32)
            case "right":
                triangle = np.array([[
                (width//2, height),
                (width, height//2),
                (width, height),]], np.int32)
            case "mid" | _:
                triangle = np.array([[
                (0, height),
                (width//2, height//2),
                (width, height),]], np.int32)
        return triangle

    def getFinalImage(self) -> np.ndarray:
        """Return the final frame with the lines found added"""
        line_image = self.display_lines(self.lane_image, self.lines)
        combo_image = cv2.addWeighted(self.image, 0.8, line_image, 1, 0)
        return combo_image

    def showImage(self, image: np.ndarray, title: str) -> None:
        """Display the frame in cv2 windows"""
        cv2.imshow(title, image)

    def showFinalImage(self) -> None:
        """Display the final frame state in cv2 windows"""
        self.showImage(self.getFinalImage(), "result")