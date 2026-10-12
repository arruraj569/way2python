import json
payload = {"user": {"name": "Mira", "roles": ["reader"]}}
text = json.dumps(payload, sort_keys=True)
restored = json.loads(text)
print(restored["user"]["roles"][0])
print(restored == payload)
