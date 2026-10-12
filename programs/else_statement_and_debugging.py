def describe_status(status):
    if 200 <= status < 300:
        return "success"
    else:
        return "investigate"

print(describe_status(200))
print(describe_status(500))
