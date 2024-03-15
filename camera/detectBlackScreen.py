import cv2
import numpy as np

class DetectBlackScreen:
    def __init__(self, frame: np.ndarray, maxWhitePixel=50) -> None:
        self.maxWhitePixel = maxWhitePixel
        self.image = frame
        self.black_image = np.copy(self.image)
        self.black_canny = self.canny(self.black_image) #Search every line with gradiant

    def canny(self, image: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        canny = np.expand_dims(np.asarray(cv2.Canny(gray, 50, 150)), axis=2)
        return canny

    def countWhitePixel(self):
        return np.count_nonzero(np.all(self.black_canny==[255,255,255], axis=2))

    def isBlack(self):
        return self.countWhitePixel() <= self.maxWhitePixel

    def showImage(self, image: np.ndarray, title: str) -> None:
        cv2.imshow(title, image)

    def showAllImage(self):
        self.showImage(self.black_image, "img")
        self.showImage(self.black_canny, "canny")
        cv2.waitKey(1)

if __name__ == "__main__":
    from cameraSettings import Camera
    c=Camera()
    c.start()
    while True:
        img = c.capture_array()
        d = DetectBlackScreen(img)
        print(d.countWhitePixel())
        d.showAllImage()