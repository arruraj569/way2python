class NormalizedName(str):
    def __new__(cls, value):
        return super().__new__(cls, value.strip().lower())

name = NormalizedName("  LOGIN  ")
print(name, isinstance(name, str))
