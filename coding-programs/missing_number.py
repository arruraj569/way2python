def missing_number(values):
    number = len(values)
    expected_total = number * (number + 1) // 2
    return expected_total - sum(values)

print(missing_number([0, 1, 3, 4]))
print(missing_number([]))
