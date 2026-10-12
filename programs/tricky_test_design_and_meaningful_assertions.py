response = {"status": 200, "user": {"id": 2, "name": "Other user"}}
print(response["status"] == 200)
print(response["user"]["id"] == 1)
