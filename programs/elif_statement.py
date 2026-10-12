def status_group(status):
    if status < 200:
        return "informational"
    elif status < 300:
        return "success"
    elif status < 400:
        return "redirect"
    else:
        return "error"

print(status_group(201), status_group(404))
