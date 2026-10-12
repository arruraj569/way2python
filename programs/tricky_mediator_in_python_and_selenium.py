events = []
def notify(sender, event):
    events.append((sender, event))

notify("save-button", "save")
print(events)
