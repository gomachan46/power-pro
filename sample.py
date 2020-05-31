from PIL import Image
import numpy as np
import cv2
import pyocr
import pyocr.builders
from pitch_type_detector import PitchTypeDetector

def cv2pil(image):
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image

def image2text(image):
    ocr_tools = pyocr.get_available_tools()
    ocr_tool = ocr_tools[0]
    return ocr_tool.image_to_string(cv2pil(image), lang="jpn", builder=pyocr.builders.TextBuilder(tesseract_layout=6))


video = cv2.VideoCapture('./input/sample.mp4')
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
width = 256
height = 50
pitch_type_params = { 'x': 512, 'y': 576 }
speed_params = { 'x': 512, 'y': 626 }
pitch_type_text = ''
speed_text = ''
pitch_type_detector = PitchTypeDetector()

for i in range(frame_count):
    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    _, threshold_image = cv2.threshold(gray, 215, 255, cv2.THRESH_BINARY)

    if pitch_type_text == '':
        ptt, pti = pitch_type_detector.detect(frame)
        if ptt != '':
            pitch_type_text = ptt
            cv2.imwrite('./output/pitch_type.jpg', pti)

    if speed_text == '':
        speed_image = threshold_image[speed_params['y'] : speed_params['y'] + height, speed_params['x'] : speed_params['x'] + width]
        st = image2text(speed_image)
        if st != '':
            speed_text = st
            cv2.imwrite('./output/speed.jpg', speed_image)

video.release()
print(f'{pitch_type_text}, {speed_text}')
