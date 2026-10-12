from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    report = Path(folder) / "result.txt"
    report.write_text("login: PASS\n", encoding="utf-8")
    print(report.read_text(encoding="utf-8").strip())
    print(report.suffix)
