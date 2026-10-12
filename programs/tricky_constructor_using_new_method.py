class Factory:
    def __new__(cls):
        return "not a Factory instance"
    def __init__(self):
        print("initializing")

value = Factory()
print(type(value).__name__)
