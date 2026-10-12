from contextlib import contextmanager
@contextmanager
def session_label():
    print("setup")
    try:
        yield "isolated session"
    finally:
        print("cleanup")

with session_label() as label:
    print(label)
