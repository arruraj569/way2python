class A:
    def label(self): return "A"
class B(A):
    def label(self): return "B"
class C(A):
    def label(self): return "C"
class D(B, C):
    pass

print(D().label())
print([cls.__name__ for cls in D.__mro__])
