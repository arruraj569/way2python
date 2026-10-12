scope = "main"
try:
    scope = "frame"
    raise ValueError("check failed")
except ValueError:
    print("failure in:", scope)
finally:
    scope = "main"
print("restored:", scope)
