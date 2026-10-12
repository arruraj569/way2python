defaults = {"Authorization": "demo", "Accept": "application/json"}
override = {"Accept": "text/plain"}
combined = {**defaults, **override}
print(combined["Accept"])
print(defaults["Accept"])
