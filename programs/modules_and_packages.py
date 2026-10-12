# Put this function in helpers.py.
def build_email(name):
    return f"{name.lower()}@example.test"

# From another file: from helpers import build_email
print(build_email("Mira"))
