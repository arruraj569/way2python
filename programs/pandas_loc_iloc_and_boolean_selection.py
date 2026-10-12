import pandas as pd
results = pd.DataFrame({"test": ["login", "search", "profile"],
                        "status": [200, 500, 404]})
failures = results.loc[results["status"] >= 400, ["test", "status"]]
print(failures["test"].tolist())
print(results.iloc[0]["test"])
