class Component:
    def __init__(self, root):
        self.root = root
    def button(self):
        return self.root + " button"

print(Component("#login-form").button())
print(Component("#profile-form").button())
