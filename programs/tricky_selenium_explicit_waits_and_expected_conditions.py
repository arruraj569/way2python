states = [{"present": True, "visible": False, "enabled": True},
          {"present": True, "visible": True, "enabled": False}]
for state in states:
    print(state["present"], state["visible"] and state["enabled"])
