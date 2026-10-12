class Count:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        if not isinstance(other, Count):
            return NotImplemented
        return Count(self.value + other.value)

print((Count(2) + Count(3)).value)
