value = 10
def change():
    try:
        value += 1
    except UnboundLocalError:
        return "local name read before assignment"
print(change())
print(value)
