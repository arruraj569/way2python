functions = [lambda: index for index in range(3)]
fixed = [lambda index=index: index for index in range(3)]
print([function() for function in functions])
print([function() for function in fixed])
