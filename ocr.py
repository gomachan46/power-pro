from PIL import Image
import cv2
import pyocr
import pyocr.builders

class Ocr:
    def __init__(self, lang='jpn', type='text'):
        tools = pyocr.get_available_tools()
        self.tool = tools[0]
        self.lang = lang
        if type == 'text':
            self.builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        elif type == 'digit':
            self.builder = pyocr.builders.DigitBuilder(tesseract_layout=6)

    def image_to_string(self, image):
        return self.tool.image_to_string(self.__cv2pil(image), lang=self.lang, builder=self.builder)

    def __cv2pil(self, image):
        new_image = image.copy()
        if new_image.ndim == 2:  # モノクロ
            pass
        elif new_image.shape[2] == 3:  # カラー
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
        elif new_image.shape[2] == 4:  # 透過
            new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
        new_image = Image.fromarray(new_image)
        return new_image
