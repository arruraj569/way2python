import numpy as np
durations = np.array([0.2, np.nan, 1.4, 0.5])
valid = durations[~np.isnan(durations)]
print(valid[valid > 0.4].tolist())
print(round(float(np.nanmean(durations)), 2))
