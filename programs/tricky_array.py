from array import array
values = array("i", [1, 2])
try:
    values.append(2.5)
except TypeError:
    print("integer array rejects a float")
print(values.tolist())
