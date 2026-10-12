names = ["report 1.txt", "report_1.txt"]
targets = [name.replace(" ", "_") for name in names]
print(targets)
print(len(targets) == len(set(targets)))
