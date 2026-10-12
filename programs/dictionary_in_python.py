user = {"id": 7, "name": "Mira", "active": True}
print(user["name"])
print(user.get("role", "reader"))
for key, value in user.items():
    print(f"{key}={value}")
