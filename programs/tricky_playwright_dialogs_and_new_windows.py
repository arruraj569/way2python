events = []
handlers = []
def emit(value):
    for handler in handlers: handler(value)
emit("first")
handlers.append(events.append)
emit("second")
print(events)
