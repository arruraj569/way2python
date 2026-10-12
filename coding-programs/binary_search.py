def binary_search(values, target):
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return None

print(binary_search([1, 3, 5, 7, 9], 7))
print(binary_search([1, 3, 5, 7, 9], 4))
