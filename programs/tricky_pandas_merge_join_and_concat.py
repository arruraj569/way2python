import pandas as pd
left = pd.DataFrame({"key": [1, 1], "test": ["a", "b"]})
right = pd.DataFrame({"key": [1, 1], "owner": ["X", "Y"]})
print(len(left.merge(right, on="key")))
try:
    left.merge(right, on="key", validate="one_to_one")
except pd.errors.MergeError:
    print("duplicate key relationship rejected")
