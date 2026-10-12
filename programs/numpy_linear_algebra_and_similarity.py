import numpy as np
first = np.array([1.0, 2.0, 3.0])
second = np.array([2.0, 4.0, 6.0])
similarity = np.dot(first, second) / (np.linalg.norm(first) * np.linalg.norm(second))
print(round(float(similarity), 3))
