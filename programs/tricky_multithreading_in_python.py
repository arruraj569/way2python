from concurrent.futures import ThreadPoolExecutor
def work(value):
    if value == 2: raise ValueError("worker failed")
    return value * 10

with ThreadPoolExecutor(max_workers=2) as pool:
    futures = [pool.submit(work, value) for value in [1, 2]]
    for future in futures:
        try: print(future.result())
        except ValueError: print("observed worker failure")
