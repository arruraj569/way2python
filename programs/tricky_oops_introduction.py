class Result:
    def __init__(self, passed):
        self.passed = passed

first = Result(True)
second = Result(True)
print(first.passed == second.passed)
print(first == second)
