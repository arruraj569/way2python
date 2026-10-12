class SmokeTemplate:
    def check(self):
        raise NotImplementedError
    def run(self):
        print("setup")
        try:
            return self.check()
        finally:
            print("cleanup")

class LoginSmoke(SmokeTemplate):
    def check(self):
        return "login passed"

print(LoginSmoke().run())
