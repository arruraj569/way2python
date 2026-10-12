def wrap(label, operation):
    def run():
        return label + "(" + operation() + ")"
    return run

action = wrap("report", wrap("trace", lambda: "login"))
print(action())
