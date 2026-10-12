import csv
from io import StringIO
text = 'name,count\n"Mira, QA",2\n'
row = next(csv.DictReader(StringIO(text)))
print(row["name"])
print(row["count"] * 2)
print(int(row["count"]) * 2)
