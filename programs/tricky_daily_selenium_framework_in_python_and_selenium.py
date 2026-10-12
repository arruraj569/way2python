def factory():
    return {"status": "Not signed in"}

first = factory()
first["status"] = "Welcome"
second = factory()
print(second["status"])
print(first is second)
