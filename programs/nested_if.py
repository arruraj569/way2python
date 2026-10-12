user = {"active": True, "role": "editor"}
if user["active"]:
    if user["role"] == "editor":
        print("Editing allowed")
    else:
        print("Read only")
else:
    print("Account disabled")
