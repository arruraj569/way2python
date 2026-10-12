documents = {"main": {"email": "outside"}, "frame": {"email": "inside"}}
print(documents["main"]["email"])
print(documents["frame"]["email"])
print(documents["main"] is documents["frame"])
