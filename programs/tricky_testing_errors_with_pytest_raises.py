def parse(text):
    return int(text)

try:
    parse(None)
except ValueError:
    print("expected validation error")
except TypeError:
    print("different error than expected")
