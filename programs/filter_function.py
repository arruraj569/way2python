statuses = [200, 201, 404, 500]
failures = list(filter(lambda status: status >= 400, statuses))
print(failures)
print([status for status in statuses if status >= 400])
