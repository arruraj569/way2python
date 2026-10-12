import sys
print("Hello, Python!")
print("Python major version:", sys.version_info.major)
print("Interpreter:", sys.executable)
print("Virtual environment:", sys.prefix != sys.base_prefix)
