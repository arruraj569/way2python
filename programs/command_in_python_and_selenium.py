class FillCommand:
    def __init__(self, fields, key, value):
        self.fields, self.key, self.value = fields, key, value
    def execute(self):
        self.fields[self.key] = self.value

fields = {}
commands = [FillCommand(fields, "name", "Mira"), FillCommand(fields, "track", "api")]
for command in commands:
    command.execute()
print(fields)
