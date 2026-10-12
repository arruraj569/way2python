dependencies = {"python_package": True, "browser_binary": False}
print(all(dependencies.values()))
dependencies["browser_binary"] = True
print(all(dependencies.values()))
