def label(tag):
    def decorate(function):
        def wrapped():
            return tag + function()
        return wrapped
    return decorate

@label("A")
@label("B")
def message():
    return "X"

print(message())
