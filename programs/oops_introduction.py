class TestResult:
    def __init__(self, name, passed):
        self.name = name
        self.passed = passed

    def label(self):
        return f"{self.name}: {'PASS' if self.passed else 'FAIL'}"

print(TestResult("login", True).label())
