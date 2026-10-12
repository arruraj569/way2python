import pandas as pd
values = pd.Series(["a", "b", "c"], index=[10, 20, 30])
print(values.loc[10:20].tolist())
print(values.iloc[0:1].tolist())
