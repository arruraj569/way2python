import pandas as pd
frame = pd.DataFrame({"time": ["2026-10-12T10:00:00Z", "2026-10-12T11:00:00Z"],
                      "failures": [2, 3]})
frame["time"] = pd.to_datetime(frame["time"], utc=True)
daily = frame.set_index("time")["failures"].resample("D").sum()
print(daily.iloc[0])
