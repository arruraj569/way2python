def apply_to_all(operation, values):
    return [operation(value) for value in values]

def milliseconds(seconds):
    return int(seconds * 1000)

print(apply_to_all(milliseconds, [0.2, 0.5, 1.0]))
