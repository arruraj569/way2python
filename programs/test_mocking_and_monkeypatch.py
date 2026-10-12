import os
def api_timeout():
    return int(os.getenv("API_TIMEOUT", "5"))

def test_timeout_override(monkeypatch):
    monkeypatch.setenv("API_TIMEOUT", "9")
    assert api_timeout() == 9
