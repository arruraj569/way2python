def broken_normalize(value):
    return ""

values = ["Mira", "LOGIN", ""]
print(all(broken_normalize(broken_normalize(value)) == broken_normalize(value) for value in values))
print(broken_normalize("Mira") == "mira")
