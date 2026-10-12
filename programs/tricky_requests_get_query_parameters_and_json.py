payload = {"id": "7", "active": "False"}
print(payload["id"] == 7)
print(bool(payload["active"]))
print(type(payload["id"]).__name__)
