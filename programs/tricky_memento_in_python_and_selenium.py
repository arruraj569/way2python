draft = {"tags": ["smoke"]}
bad_snapshot = draft
draft["tags"].append("edited")
print(bad_snapshot["tags"])
