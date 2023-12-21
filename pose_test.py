from ultralytics import YOLO
import numpy as np

model = YOLO('yolov8m-pose.pt')

results1 = model(source='tpose/IMG_8665.jpg', show=True, conf=0.3, save=True)
results2 = model(source='tpose/IMG_8666.jpg', show=True, conf=0.3, save=True)


#print(results[0].keypoints.numpy)

keys1 = np.array(results1[0].keypoints.xy)
keys2 = np.array(results2[0].keypoints.xy)
