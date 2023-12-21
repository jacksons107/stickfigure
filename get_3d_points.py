import cv2 as cv
from viewer import proj1, proj2
from pose_test import keys1, keys2


points_4hd = cv.triangulatePoints(proj1, proj2, keys1, keys2)

points_4hd /= points_4hd[3]
points_3d = points_4hd[:3].T

print(points_3d)
