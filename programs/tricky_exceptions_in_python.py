def result():
    try:
        return "from try"
    finally:
        return "from finally"

print(result())
