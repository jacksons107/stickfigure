import pickle
import numpy as np

with open('cameraMatrix.pkl', 'rb') as file:
    object = pickle.load(file)

#print(type(object))

ext1 = np.array([[1, 0, 0, 0],
               [0, 1, 0, -1016],
               [0, 0, 1, -2438.4]])

proj1 = np.matmul(object, ext1)

ext2 = np.array([[1, 0, 0, 1016],
               [0, 1, 0, 0],
               [0, 0, 1, -2438.4]])

proj2 = np.matmul(object, ext2)

#print(proj)