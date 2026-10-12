def two_sum(values, target):
    seen = {}
    for index, value in enumerate(values):
        needed = target - value
        if needed in seen:
            return seen[needed], index
        seen[value] = index
    return None

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 3], 6))
print(two_sum([3], 6))
