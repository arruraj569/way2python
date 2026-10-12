raw = "12.0"
try:
    print(int(raw))
except ValueError:
    print("not an integer literal")
print(int(float(raw)))
