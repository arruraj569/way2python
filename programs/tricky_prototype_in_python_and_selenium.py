original = {"tags": ["smoke"]}
clone = original.copy()
clone["tags"].append("regression")
print(original["tags"])
print(original is clone)
