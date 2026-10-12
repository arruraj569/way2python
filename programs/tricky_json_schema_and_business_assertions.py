payload = {"id": True, "name": "Other user"}
print(isinstance(payload["id"], int))
print(type(payload["id"]) is int)
print(payload["name"] == "Mira")
