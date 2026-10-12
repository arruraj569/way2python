from concurrent.futures import ThreadPoolExecutor
def build(worker):
    return f"user-{worker}@example.test"

with ThreadPoolExecutor(max_workers=3) as pool:
    emails = list(pool.map(build, range(3)))
print(len(emails) == len(set(emails)))
print(emails)
