class Settings:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    @property
    def timeout(self):
        return 5

first, second = Settings(), Settings()
print(first is second)
print(first.timeout)
