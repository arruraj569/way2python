requirements = {"bindings": True, "browser": True, "driver": False}
print("Ready:", all(requirements.values()))
requirements["driver"] = True
print("Ready:", all(requirements.values()))
