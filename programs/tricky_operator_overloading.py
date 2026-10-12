class Amount:
    def __init__(self, value): self.value = value
    def __add__(self, other):
        if not isinstance(other, Amount): return NotImplemented
        return Amount(self.value + other.value)

print((Amount(2) + Amount(3)).value)
try:
    Amount(2) + 3
except TypeError:
    print("unsupported operands")
