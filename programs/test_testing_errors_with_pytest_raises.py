import pytest
def workers(value):
    if value < 1:
        raise ValueError("workers must be positive")
    return value

def test_reject_zero_workers():
    with pytest.raises(ValueError, match="must be positive"):
        workers(0)
