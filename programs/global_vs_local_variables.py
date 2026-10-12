default_timeout = 10

def adjusted_timeout(extra):
    timeout = default_timeout + extra
    return timeout

print(adjusted_timeout(5))
print(default_timeout)
