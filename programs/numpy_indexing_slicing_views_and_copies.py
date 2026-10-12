import numpy as np
values = np.array([10, 20, 30, 40])
view = values[1:3]
independent = view.copy()
view[0] = 99
print(values.tolist())
print(independent.tolist())
