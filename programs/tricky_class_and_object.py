class Suite:
    tests = []

first, second = Suite(), Suite()
first.tests.append("login")
print(second.tests)
print(first.tests is second.tests)
