import csv
from io import StringIO
text = "name,expected\nvalid,201\ninvalid,422\n"
cases = list(csv.DictReader(StringIO(text)))
for case in cases:
    print(case["name"], int(case["expected"]))
