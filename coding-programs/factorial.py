def factorial(number):
    if type(number) is not int or number < 0:
        raise ValueError("use a nonnegative integer")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

print(factorial(0), factorial(5))
