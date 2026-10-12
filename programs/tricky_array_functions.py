from array import array
values = array("i", [1, 2])
result = values.extend([3, 4])
print(result)
print(values.pop())
print(values.tolist())
