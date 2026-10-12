def unique_in_order(values):
    seen, result = set(), []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result

print(unique_in_order([3, 1, 3, 2, 1]))
