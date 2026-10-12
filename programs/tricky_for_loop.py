pairs = list(zip([1, 2, 3], ["a", "b"]))
print(pairs)
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))
except ValueError:
    print("length mismatch")
