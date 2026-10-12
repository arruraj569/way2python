import pandas as pd
frame = pd.DataFrame({"browser": ["chrome", "chrome", "firefox"],
                      "seconds": [1.0, 3.0, 2.0]})
summary = frame.groupby("browser")["seconds"].agg(["count", "mean"])
print(summary["count"].to_dict())
print(summary["mean"].to_dict())
