results = [{"name": "health", "passed": True}, {"name": "create", "passed": False}]
exit_code = 0 if all(result["passed"] for result in results) else 1
print("Report rows:", len(results))
print("Required exit code:", exit_code)
