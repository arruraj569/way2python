existing = {1: "another test", 2: "my test"}
owned_ids = {2}
for identity in owned_ids:
    existing.pop(identity, None)
print(existing)
