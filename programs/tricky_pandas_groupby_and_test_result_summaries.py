import pandas as pd
frame = pd.DataFrame({"browser": ["chromium", None], "count": [1, 1]})
print(int(frame.groupby("browser")["count"].sum().sum()))
print(int(frame.groupby("browser", dropna=False)["count"].sum().sum()))
