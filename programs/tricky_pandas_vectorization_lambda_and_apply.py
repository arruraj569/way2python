import numpy as np
import pandas as pd
values = pd.Series([0.5, 1.5])
classify = lambda value: "slow" if value > 1 else "normal"
print(values.apply(classify).tolist())
try:
    classify(np.array([0.5, 1.5]))
except ValueError:
    print("array truth value is ambiguous")
