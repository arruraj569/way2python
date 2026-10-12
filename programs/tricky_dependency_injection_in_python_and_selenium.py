class Reader:
    def __init__(self, read):
        self.read = read

values = ["old"]
reader = Reader(lambda: values[0])
values[0] = "new"
print(reader.read())
