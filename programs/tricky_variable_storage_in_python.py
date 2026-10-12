import copy
original = {"tags": ["smoke"]}
shallow = original.copy()
deep = copy.deepcopy(original)
shallow["tags"].append("api")
print(original["tags"])
print(deep["tags"])
print(shallow is original)
