def workflow(check):
    try:
        check()
    finally:
        print("cleanup")

try:
    workflow(lambda: 1 / 0)
except ZeroDivisionError:
    print("failure preserved")
