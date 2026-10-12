status = 201
payload = {"id": 12, "name": "Mira"}
assert 200 <= status < 300
assert "id" in payload and payload["id"] > 0
print(status == 201, "email" not in payload)
