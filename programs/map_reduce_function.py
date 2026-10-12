from functools import reduce
durations = [0.2, 0.5, 0.3]
print(list(map(lambda value: int(value * 1000), durations)))
product = reduce(lambda total, value: total * value, [2, 3, 4], 1)
print(product)
print(sum(durations))
