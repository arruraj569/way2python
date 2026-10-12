user = {"authenticated": True, "role": "reader"}
print(user["authenticated"])
print(user["authenticated"] and user["role"] == "admin")
