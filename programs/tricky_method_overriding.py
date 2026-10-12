class Base:
    def label(self): return "base"
    def describe(self): return self.label()
class Child(Base):
    def label(self): return "child"

print(Child().describe())
print(Base.label(Child()))
