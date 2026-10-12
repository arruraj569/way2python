run_a = {"login", "checkout", "search"}
run_b = {"login", "search", "profile"}
print(sorted(run_a & run_b))
print(sorted(run_a - run_b))
