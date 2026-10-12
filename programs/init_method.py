class ApiConfig:
    def __init__(self, base_url, timeout=5):
        if timeout <= 0:
            raise ValueError("timeout must be positive")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

config = ApiConfig("http://127.0.0.1:8765/")
print(config.base_url, config.timeout)
