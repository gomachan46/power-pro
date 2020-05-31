from ocr import Ocr
import cv2

class PitchTypeDetector:
    THRESHOLD_VALUE = 220
    THRESHOLD_MAX_VALUE = 255
    X = 512
    Y = 576
    WIDTH = 256
    HEIGHT = 50

    def __init__(self):
        self.ocr = Ocr()

    def detect(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, self.THRESHOLD_VALUE, self.THRESHOLD_MAX_VALUE, cv2.THRESH_BINARY)

        pitch_type_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X : self.X + self.WIDTH]
        pitch_type = self.ocr.image_to_string(pitch_type_image)

        return pitch_type, pitch_type_image
