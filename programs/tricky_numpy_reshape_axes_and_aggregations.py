import numpy as np
values = np.array([[1, 2, 3], [4, 5, 6]])
print(values.sum(axis=0).tolist())
print(values.sum(axis=1).tolist())
print(values.sum(axis=1, keepdims=True).shape)
