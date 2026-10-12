def parse_workers(text):
    workers = int(text)
    if workers < 1:
        raise ValueError("workers must be positive")
    return workers

print(parse_workers("4"))
# Interactive use: parse_workers(input("Workers: "))
