def login_cases():
    yield {"name": "valid", "expected": "Welcome"}
    yield {"name": "invalid", "expected": "Rejected"}

cases = login_cases()
print(next(cases)["name"])
print([case["name"] for case in cases])
print(list(cases))
print([case["name"] for case in login_cases()])
