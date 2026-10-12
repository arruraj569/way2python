import pandas as pd
frame = pd.DataFrame({"name": ["Mira", "Mira", "Arun"],
                      "duration": [1.0, 1.0, None]})
unique = frame.drop_duplicates()
print(len(unique))
print(unique["duration"].isna().sum())
print(unique["duration"].fillna(0).tolist())
