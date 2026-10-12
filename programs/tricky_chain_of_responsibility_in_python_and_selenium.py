handlers = [(Exception, "general"), (TimeoutError, "timeout")]
error = TimeoutError()
print(next(label for kind, label in handlers if isinstance(error, kind)))
