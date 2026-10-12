from concurrent.futures import ThreadPoolExecutor
def label(number):
    return f"case-{number}"

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(label, [1, 2, 3]))
print(results)
