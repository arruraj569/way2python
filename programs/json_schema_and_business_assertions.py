from jsonschema import Draft202012Validator
schema = {"type": "object", "required": ["id", "name", "email"],
          "properties": {"id": {"type": "integer", "minimum": 1},
                         "name": {"type": "string", "minLength": 1},
                         "email": {"type": "string"}}}
payload = {"id": 1, "name": "Mira", "email": "mira@example.test"}
Draft202012Validator(schema).validate(payload)
assert payload["name"] == "Mira"
print("Shape and value checks passed")
