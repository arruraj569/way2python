from pathlib import Path
files = [Path("report 1.txt"), Path("report 2.txt")]
for source in files:
    target = source.with_name(source.name.replace(" ", "_"))
    print(f"DRY RUN: {source} -> {target}")
