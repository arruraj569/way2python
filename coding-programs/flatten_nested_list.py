def flatten(values):
    result = []
    def visit(items):
        for item in items:
            if isinstance(item, list):
                visit(item)
            else:
                result.append(item)
    visit(values)
    return result

print(flatten([1, [2, [3], []], 4]))
