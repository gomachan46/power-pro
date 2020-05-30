import numpy as np
import cv2

video = cv2.VideoCapture('./input/sample.mp4')
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
writer = cv2.VideoWriter('./output/sample.mp4', fmt, fps, size)

for i in range(frame_count):
    ret, frame = video.read()
    writer.write(frame)

video.release()
writer.release()
cv2.destroyAllWindows()
