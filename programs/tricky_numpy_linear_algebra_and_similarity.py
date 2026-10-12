import numpy as np
left = np.array([[1, 2], [3, 4]])
right = np.array([[2, 0], [0, 2]])
print((left * right).tolist())
print((left @ right).tolist())
