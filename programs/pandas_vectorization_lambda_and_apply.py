import pandas as pd
frame = pd.DataFrame({"seconds": [0.2, 1.5, 0.8]})
frame["milliseconds"] = frame["seconds"] * 1000
frame["label"] = frame["seconds"].apply(lambda value: "slow" if value > 1 else "normal")
print(frame["milliseconds"].tolist())
print(frame["label"].tolist())
