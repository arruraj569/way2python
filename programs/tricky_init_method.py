class Config:
    def __init__(self):
        self.timeout = 5
        return "ready"

try:
    Config()
except TypeError:
    print("__init__ must return None")
