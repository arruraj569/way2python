import pandas as pd
values = pd.Series([1, pd.NA], dtype="Int64")
print(values.isna().tolist())
try:
    bool(pd.NA)
except TypeError:
    print("missing truth value is ambiguous")
print(values.fillna(0).tolist())
