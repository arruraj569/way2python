def exact(actual, expected):
    return actual == expected

def normalized(actual, expected):
    return actual.strip().casefold() == expected.strip().casefold()

class TextCheck:
    def __init__(self, strategy):
        self.strategy = strategy
    def matches(self, actual, expected):
        return self.strategy(actual, expected)

print(TextCheck(exact).matches(" Mira ", "mira"))
print(TextCheck(normalized).matches(" Mira ", "mira"))
