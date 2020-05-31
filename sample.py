import cv2
from pitch_type_detector import PitchTypeDetector
from speed_detector import SpeedDetector

video = cv2.VideoCapture('./input/sample.mp4')
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
pitch_type_detector = PitchTypeDetector()
speed_detector = SpeedDetector()

pitch_type_text = ''
speed_text = ''

for i in range(frame_count):
    _, frame = video.read()
    if pitch_type_text == '':
        ptt, pti = pitch_type_detector.detect(frame)
        if ptt != '':
            pitch_type_text = ptt
            cv2.imwrite('./output/pitch_type.jpg', pti)

    if speed_text == '':
        st, si = speed_detector.detect(frame)
        if st != '':
            speed_text = st
            cv2.imwrite('./output/speed.jpg', si)

video.release()
print(f'{pitch_type_text}, {speed_text}')
