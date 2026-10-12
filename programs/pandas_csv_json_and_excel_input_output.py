import pandas as pd
from io import StringIO
text = "case_id,status\n001,200\n002,500\n"
frame = pd.read_csv(StringIO(text), dtype={"case_id": "string"})
print(frame["case_id"].tolist())
print(frame.to_csv(index=False).strip())
