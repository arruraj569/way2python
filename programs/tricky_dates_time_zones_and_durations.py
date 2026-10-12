from datetime import datetime, timezone
naive = datetime(2026, 10, 12, 10)
aware = datetime(2026, 10, 12, 10, tzinfo=timezone.utc)
try:
    print(aware - naive)
except TypeError:
    print("cannot subtract aware and naive timestamps")
