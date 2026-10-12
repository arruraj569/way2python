def countdown(n):
    if n <= 0:
        return [0]
    return [n] + countdown(n - 1)

print(countdown(3))
