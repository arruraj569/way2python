def total(values):
    if not values:
        return 0
    return values[0] + total(values[1:])

print(total([]))
print(total([1, 2, 3]))
