from contextlib import contextmanager
@contextmanager
def fixture_like():
    print("setup")
    try: yield []
    finally: print("teardown")

try:
    with fixture_like() as values:
        values.append(1)
        assert len(values) == 0
except AssertionError:
    print("test failed")
