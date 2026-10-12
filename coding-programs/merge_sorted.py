def merge_sorted(left, right):
    first = second = 0
    result = []
    while first < len(left) and second < len(right):
        if left[first] <= right[second]:
            result.append(left[first])
            first += 1
        else:
            result.append(right[second])
            second += 1
    result.extend(left[first:])
    result.extend(right[second:])
    return result

print(merge_sorted([1, 3, 5], [2, 4]))
print(merge_sorted([], [1, 1]))
