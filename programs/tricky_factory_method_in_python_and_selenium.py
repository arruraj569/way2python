def fresh_driver_double():
    return {"cookies": []}

first, second = fresh_driver_double(), fresh_driver_double()
first["cookies"].append("session-a")
print(first is second)
print(second["cookies"])
