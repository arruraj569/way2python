payloads = [{}, {"name": None}, {"name": ""}, {"name": " "}]
for payload in payloads:
    present = "name" in payload
    value = payload.get("name")
    valid = isinstance(value, str) and bool(value.strip())
    print(present, valid)
