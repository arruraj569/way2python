import pandas as pd
tests = pd.DataFrame({"suite": ["auth", "catalog"], "failures": [2, 1]})
owners = pd.DataFrame({"suite": ["auth", "catalog"], "owner": ["Team A", "Team B"]})
joined = tests.merge(owners, on="suite", how="left", validate="one_to_one")
print(joined["owner"].tolist())
