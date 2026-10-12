from functools import reduce
mapped = map(lambda value: value * 2, [1, 2, 3])
print(next(mapped))
print(list(mapped))
print(reduce(lambda a, b: a + b, [], 0))
