import cv2
from pitch_type_detector import PitchTypeDetector
from speed_detector import SpeedDetector
import os

def analyze(pathname, filename):
    video = cv2.VideoCapture(os.path.join(pathname, filename))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    pitch_type_detector = PitchTypeDetector()
    speed_detector = SpeedDetector()

    pitch_type_text = ''
    pitch_type_image = None
    speed_text = ''
    speed_image = None

    for i in range(frame_count):
        _, frame = video.read()
        ptt, pti = pitch_type_detector.detect(frame)
        # 球種表示で動画が終わらないのもままあるので雑なパッチにしてる
        if ptt == 'ストレート' or ptt == 'チェンジアップ':
            pitch_type_text = ptt
            pitch_type_image = pti
            speed_text, speed_image = speed_detector.detect(frame)

    video.release()

    if pitch_type_text == '' or speed_text == '':
        print(f'{filename} うまく検出できなかったぽい')
        return

    print(f'{filename}, {pitch_type_text}, {speed_text}')
    cv2.imwrite(f'./output/{filename}_pitch_type.jpg', pitch_type_image)
    cv2.imwrite(f'./output/{filename}_speed.jpg', speed_image)

for pathname, dirnames, filenames in os.walk('input'):
    for filename in filenames:
        if filename.endswith('.mp4'):
            analyze(pathname, filename)