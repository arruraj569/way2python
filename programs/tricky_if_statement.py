status = 200
if status == 200 or 201:
    print("accepted")
status = 500
print(bool(status == 200 or 201))
print(status in {200, 201})
