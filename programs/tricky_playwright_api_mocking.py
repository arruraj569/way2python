import json
payload = {"name": "Mira"}
try:
    json.loads(str(payload))
except json.JSONDecodeError:
    print("repr is not JSON")
print(json.loads(json.dumps(payload))["name"])
