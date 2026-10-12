old_record = {"name": "before"}
current_record = old_record
current_record = {"name": "after"}
print(old_record["name"], current_record["name"])
print(old_record is current_record)
