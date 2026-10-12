cases = [(1, True), (0, False), (-1, False)]
for value, expected in cases:
    actual = value > 0
    print(value, actual == expected)
print(len(cases))
