listeners = []
def once(event):
    listeners.remove(once)
    print(event)

listeners.append(once)
for listener in tuple(listeners):
    listener("finished")
print(len(listeners))
