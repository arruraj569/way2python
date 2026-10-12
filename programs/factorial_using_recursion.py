def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("use a nonnegative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
