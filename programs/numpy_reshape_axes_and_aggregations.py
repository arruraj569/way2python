import numpy as np
durations = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(durations.shape)
print(durations.mean(axis=0).tolist())
print(durations.sum(axis=1).tolist())
