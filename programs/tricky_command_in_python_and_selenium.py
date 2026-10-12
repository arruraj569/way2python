commands = [lambda: number for number in range(3)]
fixed = [lambda number=number: number for number in range(3)]
print([command() for command in commands])
print([command() for command in fixed])
