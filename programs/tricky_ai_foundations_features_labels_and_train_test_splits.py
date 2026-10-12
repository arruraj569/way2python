records = [{"source": "A", "row": 1}, {"source": "A", "row": 2}, {"source": "B", "row": 3}]
train, test = records[:1], records[1:]
overlap = {row["source"] for row in train} & {row["source"] for row in test}
print(sorted(overlap))
print(bool(overlap))
