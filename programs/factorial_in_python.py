def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("use a nonnegative integer")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result

print(factorial(0), factorial(5))
