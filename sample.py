import numpy as np
import cv2

video = cv2.VideoCapture('./input/sample.mp4')
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
writer = cv2.VideoWriter('./output/sample.mp4', fmt, fps, size, False)

for i in range(frame_count):
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret, threshold_image = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)
    writer.write(threshold_image)

video.release()
writer.release()
