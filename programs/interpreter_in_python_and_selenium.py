class Equals:
    def __init__(self, key, value):
        self.key, self.value = key, value
    def evaluate(self, record):
        return record.get(self.key) == self.value

class And:
    def __init__(self, expressions):
        self.expressions = expressions
    def evaluate(self, record):
        return all(item.evaluate(record) for item in self.expressions)

def parse(rule):
    expressions = []
    for term in rule.split(" AND "):
        if term.count("=") != 1:
            raise ValueError("expected key=value")
        key, value = term.split("=")
        if key not in {"status", "track"} or not value:
            raise ValueError("unsupported rule")
        expressions.append(Equals(key, value))
    return And(expressions)

expression = parse("status=passed AND track=selenium")
print(expression.evaluate({"status": "passed", "track": "selenium"}))
print(expression.evaluate({"status": "failed", "track": "selenium"}))
