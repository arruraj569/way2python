def fibonacci(length):
    if type(length) is not int or length < 0:
        raise ValueError("length must be a nonnegative integer")
    first, second = 0, 1
    result = []
    for _ in range(length):
        result.append(first)
        first, second = second, first + second
    return result

print(fibonacci(8))
print(fibonacci(0))
