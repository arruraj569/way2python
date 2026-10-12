names = ["login", "search", "profile"]
statuses = [200, 500, 200]
failed = [name for name, status in zip(names, statuses, strict=True)
          if status >= 400]
print(failed)
print({name: index for index, name in enumerate(names, 1)})
