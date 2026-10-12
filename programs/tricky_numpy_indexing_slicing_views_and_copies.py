import numpy as np
values = np.array([10, 20, 30])
basic = values[:2]
advanced = values[[0, 1]]
basic[0] = 99
advanced[1] = 77
print(values.tolist())
print(advanced.tolist())
