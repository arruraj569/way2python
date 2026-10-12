def second_largest(values):
    largest = second = None
    for value in values:
        if largest is None or value > largest:
            second, largest = largest, value
        elif value != largest and (second is None or value > second):
            second = value
    return second

print(second_largest([5, 5, 3, 2]))
print(second_largest([-4, -2, -3]))
print(second_largest([5, 5]))
