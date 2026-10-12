def twice(function, value):
    return function(function(value))

print(twice(lambda value: value + 1, 3))
print(twice(str.upper, "python"))
