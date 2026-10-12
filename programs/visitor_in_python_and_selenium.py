class FillStep:
    def __init__(self, field):
        self.field = field
    def accept(self, visitor):
        return visitor.visit_fill(self)

class ClickStep:
    def __init__(self, button):
        self.button = button
    def accept(self, visitor):
        return visitor.visit_click(self)

class DescriptionVisitor:
    def visit_fill(self, step):
        return "fill " + step.field
    def visit_click(self, step):
        return "click " + step.button

visitor = DescriptionVisitor()
print([step.accept(visitor) for step in [FillStep("name"), ClickStep("save")]])
