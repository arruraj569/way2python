import numpy as np
values = np.array([1.0, np.nan, 3.0])
print((values == np.nan).tolist())
print(np.isnan(values).tolist())
print(float(np.nanmean(values)))
