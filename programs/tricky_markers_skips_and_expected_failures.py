reported = ["passed", "skipped", "xfail", "passed"]
print("Failures:", reported.count("failed"))
print("Executed passes:", reported.count("passed"))
print("Total:", len(reported))
