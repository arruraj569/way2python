import os
base_url = os.getenv("API_BASE_URL", "http://127.0.0.1:8765")
timeout = float(os.getenv("API_TIMEOUT", "5"))
if timeout <= 0:
    raise ValueError("API_TIMEOUT must be positive")
print(base_url, timeout)
