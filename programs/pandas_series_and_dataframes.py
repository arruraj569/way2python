import pandas as pd
results = pd.DataFrame({"test": ["login", "search"],
                        "passed": [True, False], "seconds": [1.2, 0.8]})
print(results.shape)
print(results["test"].tolist())
print(results["seconds"].mean())
