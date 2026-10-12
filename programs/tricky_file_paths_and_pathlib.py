from pathlib import Path
parent = Path("reports")
print(str(parent / "result.txt"))
print(str(parent / Path("/tmp/result.txt")))
print(Path("archive.tar.gz").suffixes)
