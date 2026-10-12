from pathlib import Path
relative = Path("sample.txt")
absolute = relative.resolve()
print(relative.is_absolute())
print(absolute.is_absolute())
