import pandas as pd
left = pd.Series([1, 2], index=["a", "b"])
right = pd.Series([10, 20], index=["b", "a"])
print((left + right).to_dict())
print((left.to_numpy() + right.to_numpy()).tolist())
