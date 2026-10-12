def parse_timeout(text):
    try:
        value = int(text)
    except ValueError as error:
        raise ValueError("timeout must be an integer") from error
    if value <= 0:
        raise ValueError("timeout must be positive")
    return value

print(parse_timeout("5"))
