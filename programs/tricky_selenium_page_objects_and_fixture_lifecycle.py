class Driver:
    def __init__(self): self.closed = False
    def quit(self): self.closed = True
driver = Driver()
try:
    raise AssertionError("failure")
except AssertionError:
    print("test failed")
finally:
    driver.quit()
print(driver.closed)
