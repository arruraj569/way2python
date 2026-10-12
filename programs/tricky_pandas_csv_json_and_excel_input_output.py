import pandas as pd
from io import StringIO
text = "id,value\n001,8\n002,9\n"
inferred = pd.read_csv(StringIO(text))
explicit = pd.read_csv(StringIO(text), dtype={"id": "string"})
print(inferred["id"].tolist())
print(explicit["id"].tolist())
