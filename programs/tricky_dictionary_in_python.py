record = {"value": None}
print(record.get("missing"))
print(record.get("value"))
print("missing" in record, "value" in record)
result = record.update({"name": "Mira"})
print(result)
