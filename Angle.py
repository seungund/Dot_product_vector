import numpy as np

vector1 = np.array([4, 2])
vector2 = np.array([3, 5])

angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
degree = np.degrees(angle)

print(degree)