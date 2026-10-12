values = ["login", "profile"]
missing = [value for value in values if value == "checkout"]
print(missing)
try:
    print(missing[0])
except IndexError:
    print("no matching item")
