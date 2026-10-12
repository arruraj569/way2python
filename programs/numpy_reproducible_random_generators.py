import numpy as np
first = np.random.default_rng(42).integers(0, 100, size=5)
second = np.random.default_rng(42).integers(0, 100, size=5)
assert np.array_equal(first, second)
print("Seeded arrays match")
