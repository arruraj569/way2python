actions = []
completed = []
actions.append(lambda: completed.append("click"))
print(completed)
for action in actions: action()
print(completed)
