from contextlib import contextmanager

@contextmanager
def resource():
    try:
        yield []
    finally:
        print("cleanup")

with resource() as items:
    items.append("done")
print(items)
