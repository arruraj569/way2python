counts = {"small_suite": (1, 2), "large_suite": (10, 100)}
for name, (failures, total) in counts.items():
    print(name, f"{failures / total:.0%}")
