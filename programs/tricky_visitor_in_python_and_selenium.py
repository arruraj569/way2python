class SaveStep:
    def accept(self, visitor):
        return visitor.visit_save(self)

class IncompleteVisitor:
    pass

print(hasattr(IncompleteVisitor(), "visit_save"))
