class LegacyField:
    def __init__(self):
        self.text = "old"
    def clear(self):
        self.text = ""
    def send_keys(self, value):
        self.text += value

class FillAdapter:
    def __init__(self, field):
        self.field = field
    def fill(self, value):
        self.field.clear()
        self.field.send_keys(value)

field = LegacyField()
FillAdapter(field).fill("Mira")
print(field.text)
