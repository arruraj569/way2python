def values():
    yield 1
    yield 2

generator = values()
print(sum(generator))
print(sum(generator))
print(sum(values()))
