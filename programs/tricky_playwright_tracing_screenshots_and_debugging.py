events = [("click", "loading"), ("response", "500"), ("screen", "error")]
print("Last screen:", events[-1][1])
print("Network evidence:", next(value for event, value in events if event == "response"))
