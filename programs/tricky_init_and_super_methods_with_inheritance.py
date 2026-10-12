class Base:
    def __init__(self): self.ready = True
class Child(Base):
    def __init__(self): self.name = "child"

child = Child()
print(hasattr(child, "name"))
print(hasattr(child, "ready"))
