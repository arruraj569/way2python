from pathlib import Path
names = [Path("results.csv"), Path("results.txt")]
content = "test,status\nlogin,passed\n"
print(names[0].suffix == ".csv")
print(content.splitlines()[0] == "test,status")
print(names[1].suffix == ".csv")
