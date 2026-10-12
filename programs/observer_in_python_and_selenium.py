class Events:
    def __init__(self):
        self.listeners = []
    def subscribe(self, listener):
        self.listeners.append(listener)
    def publish(self, event):
        for listener in tuple(self.listeners):
            listener(event)

records = []
events = Events()
events.subscribe(lambda event: print("log:", event))
events.subscribe(records.append)
events.publish("login passed")
print(records)
