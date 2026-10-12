class ResultReader:
    def __init__(self, read_text):
        self.read_text = read_text
    def passed(self):
        return self.read_text() == "Welcome, learner!"

success_reader = ResultReader(lambda: "Welcome, learner!")
failure_reader = ResultReader(lambda: "Invalid credentials")
print(success_reader.passed())
print(failure_reader.passed())
