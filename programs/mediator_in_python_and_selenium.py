class NameField:
    def __init__(self, value):
        self.value = value

class SaveButton:
    def __init__(self, mediator):
        self.mediator = mediator
    def click(self):
        return self.mediator.notify(self, "save")

class ProfileMediator:
    def __init__(self, field):
        self.field = field
    def notify(self, sender, event):
        if event != "save":
            raise ValueError("unknown event")
        return "saved " + self.field.value if self.field.value.strip() else "name required"

field = NameField("Mira")
button = SaveButton(ProfileMediator(field))
print(button.click())
field.value = " "
print(button.click())
