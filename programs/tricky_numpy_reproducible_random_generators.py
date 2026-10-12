import numpy as np
generator = np.random.default_rng(42)
first = generator.integers(0, 100, 5)
second = generator.integers(0, 100, 5)
restarted = np.random.default_rng(42).integers(0, 100, 5)
print(np.array_equal(first, second))
print(np.array_equal(first, restarted))
