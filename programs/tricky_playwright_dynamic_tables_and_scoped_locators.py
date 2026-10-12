rows = [{"task": "login", "done": False}, {"task": "API", "done": False}]
rows.sort(key=lambda row: row["task"])
print(rows[0]["task"])
selected = next(row for row in rows if row["task"] == "login")
print(selected["task"])
