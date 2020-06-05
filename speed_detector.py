from ocr import Ocr
import cv2

class SpeedDetector:
    THRESHOLD_VALUE = 225 # 極力ノイズを取って文字認識の結果を安定させる狙いで高めのチューニングにしている
    THRESHOLD_MAX_VALUE = 255
    X = 575
    Y = 626
    WIDTH = 25
    HEIGHT = 50

    def __init__(self):
        self.ocr = Ocr(lang='eng', type='digit')

    def detect(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, threshold_image = cv2.threshold(gray_image, self.THRESHOLD_VALUE, self.THRESHOLD_MAX_VALUE, cv2.THRESH_BINARY)

        # 一桁ずつ認識させることで揺らぎ率を下げる狙い
        one_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X + self.WIDTH * 0 : self.X + self.WIDTH * 1]
        one_speed = self.__image_to_string(one_image, allow_blank=True)
        two_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X + self.WIDTH * 1: self.X + self.WIDTH * 2]
        two_speed = self.__image_to_string(two_image)
        if one_speed == '1' and two_speed == '9':
            two_speed = '0'
        elif one_speed == '' and two_speed == '0':
            two_speed = '9'
        if one_speed == '' and int(two_speed) < 5:
            one_speed = '1'
        three_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X + self.WIDTH * 2 : self.X + self.WIDTH * 3]
        three_speed = self.__image_to_string(three_image)

        speed_image = threshold_image[self.Y : self.Y + self.HEIGHT, self.X : self.X + self.WIDTH * 3]

        return one_speed + two_speed + three_speed, speed_image

    def __image_to_string(self, image, allow_blank=False):
        speed = self.ocr.image_to_string(image)
        if allow_blank and speed == '':
            return ''

        # ここはもうパターン列挙で精度を上げにかかる
        # 上手く行かない数字があったらマッピングしてあげる
        if speed.startswith('q', 0) or speed.startswith('0', 0):
            return '0'
        elif speed == '|' or speed == 'i' or speed == '':
            return '1'
        elif speed.startswith('r', 0) or speed == '=':
            return '2'
        elif speed.startswith('E', 0):
            return '3'
        elif speed.startswith('u', 0) or speed == 'A' or speed == 'cs':
            return '4'
        elif speed == '=)':
            return '5'
        elif speed == 'J' or speed == ']':
            return '6'
        elif speed.endswith(')') or speed == 'S':
            return '9'

        return speed
