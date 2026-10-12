def counter():
    value = 0
    def increment():
        nonlocal value
        value += 1
        return value
    return increment

first, second = counter(), counter()
print(first(), first(), second())
