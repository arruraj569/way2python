left, right = [1], [2]
old_left = left
left, right = right, left
old_left.append(3)
print(left, right)
