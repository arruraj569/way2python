def action(command):
    match command:
        case "smoke":
            return "run critical tests"
        case "full":
            return "run every test"
        case _:
            return "unknown command"

print(action("smoke"))
