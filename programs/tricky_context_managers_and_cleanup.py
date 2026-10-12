from contextlib import contextmanager
@contextmanager
def resource():
    print("open")
    try: yield
    finally: print("close")

try:
    with resource():
        raise ValueError("broken")
except ValueError:
    print("failure preserved")
