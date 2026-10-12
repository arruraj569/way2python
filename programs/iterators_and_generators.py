def batches(values, size):
    if size < 1:
        raise ValueError("size must be positive")
    for start in range(0, len(values), size):
        yield values[start:start + size]

print(list(batches([1, 2, 3, 4, 5], 2)))
