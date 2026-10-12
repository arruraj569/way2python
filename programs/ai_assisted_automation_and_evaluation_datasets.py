reviewed = [
    {"expected": "timeout", "predicted": "timeout"},
    {"expected": "authorization", "predicted": "timeout"},
    {"expected": "validation", "predicted": "validation"},
]
correct = sum(row["expected"] == row["predicted"] for row in reviewed)
print(f"Reviewed label agreement: {correct}/{len(reviewed)}")
assert all(row["predicted"] in {"timeout", "authorization", "validation"} for row in reviewed)
