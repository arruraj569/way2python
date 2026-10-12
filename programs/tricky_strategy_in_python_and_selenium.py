def exact(a, b):
    return a == b

selected = exact
print(callable(selected))
print(selected("Welcome", "welcome"))
