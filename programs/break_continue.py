for status in [200, 204, 404, 500]:
    if status == 204:
        continue
    if status >= 500:
        print("Stop at server error")
        break
    print(status)
print("Loop finished")
