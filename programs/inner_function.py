def prefixer(prefix):
    def label(name):
        return f"{prefix}:{name}"
    return label

smoke_label = prefixer("smoke")
print(smoke_label("login"))
