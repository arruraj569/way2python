settings = {"TIMEOUT": "0", "ENABLED": "False"}
print(settings["TIMEOUT"] or "5")
print(bool(settings["ENABLED"]))
print(settings["ENABLED"].lower() == "true")
