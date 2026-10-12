from functools import wraps
def announce(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper

@announce
def add_values(a, b):
    return a + b

print(add_values(2, 3))
