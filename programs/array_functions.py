from array import array
counts = array("i", [2, 4])
counts.append(6)
counts.insert(0, 1)
removed = counts.pop()
print(counts.tolist(), removed)
