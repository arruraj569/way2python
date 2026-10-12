class Base:
    @classmethod
    def name(cls):
        return cls.__name__
    @staticmethod
    def fixed():
        return "Base"
class Child(Base):
    pass

print(Child.name(), Child.fixed())
