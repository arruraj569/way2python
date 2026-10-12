class Shared:
    _instance = None
    def __new__(cls, value):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, value):
        self.value = value

first = Shared("Chrome")
second = Shared("Firefox")
print(first is second)
print(first.value)
