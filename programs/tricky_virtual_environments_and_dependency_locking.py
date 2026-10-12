from importlib import metadata
import sys
print("Python:", sys.version_info.major)
try:
    version = metadata.version("pytest")
    print("pytest installed:", bool(version))
except metadata.PackageNotFoundError:
    print("pytest installed:", False)
