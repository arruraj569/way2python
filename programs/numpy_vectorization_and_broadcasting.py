import numpy as np
samples = np.array([[1.0, 10.0], [3.0, 20.0]])
feature_means = samples.mean(axis=0)
centered = samples - feature_means
print(feature_means.tolist())
print(centered.tolist())
