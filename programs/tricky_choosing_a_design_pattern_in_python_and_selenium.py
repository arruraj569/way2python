handlers = {"login": lambda: "signed in"}
handler = handlers.get("logout")
print(handler is None)
print(handler() if handler else "unsupported operation")
