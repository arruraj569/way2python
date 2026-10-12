import json
original = {1: "one", "items": (2, 3)}
restored = json.loads(json.dumps(original))
print(restored["1"])
print(type(restored["items"]).__name__)
print(original == restored)
