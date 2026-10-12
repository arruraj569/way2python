from importlib import metadata
import sys
print("Interpreter:", sys.executable)
for name in ["pytest", "requests", "numpy", "pandas"]:
    try:
        print(name, metadata.version(name))
    except metadata.PackageNotFoundError:
        print(name, "not installed in this interpreter")
