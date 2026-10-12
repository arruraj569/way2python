import numpy as np
row = np.array([1, 2, 3])
column = row.reshape(3, 1)
result = row + column
print(result.shape)
print(result.tolist())
