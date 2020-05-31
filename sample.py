import cv2
from pitch_type_detector import PitchTypeDetector
from speed_detector import SpeedDetector

video = cv2.VideoCapture('./input/sample.mp4')
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
pitch_type_detector = PitchTypeDetector()
speed_detector = SpeedDetector()

pitch_type_text = ''
pitch_type_image = None
speed_text = ''
speed_image = None

for i in range(frame_count):
    _, frame = video.read()
    pitch_type_text, pitch_type_image = pitch_type_detector.detect(frame)
    speed_text, speed_image = speed_detector.detect(frame)

video.release()
print(f'{pitch_type_text}, {speed_text}')
cv2.imwrite('./output/pitch_type.jpg', pitch_type_image)
cv2.imwrite('./output/speed.jpg', speed_image)
