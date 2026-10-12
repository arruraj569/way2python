import pytest
@pytest.mark.smoke
def test_health():
    assert 2 + 2 == 4

# pytest.ini:
# [pytest]
# markers =
#     smoke: critical checks
# Run: python -m pytest -m smoke --strict-markers
