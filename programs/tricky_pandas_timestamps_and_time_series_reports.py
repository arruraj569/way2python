import pandas as pd
timestamp = pd.Timestamp("2026-10-12T20:00:00Z")
local = timestamp.tz_convert("Asia/Kolkata")
print(timestamp.date())
print(local.date())
