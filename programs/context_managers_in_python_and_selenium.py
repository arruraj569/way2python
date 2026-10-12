from contextlib import contextmanager

@contextmanager
def browser_double():
    print("open")
    try:
        yield "driver double"
    finally:
        print("quit")

try:
    with browser_double() as driver:
        print(driver)
        raise ValueError("failed check")
except ValueError:
    print("failure reached the test")
