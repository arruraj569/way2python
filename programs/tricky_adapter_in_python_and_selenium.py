class Field:
    text = "old"
    def send_keys(self, value):
        self.text += value

field = Field()
field.send_keys("new")
print(field.text)
