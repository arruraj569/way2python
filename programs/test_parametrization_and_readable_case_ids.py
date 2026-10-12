import pytest
@pytest.mark.parametrize("raw, expected", [
    ("  Mira  ", "mira"),
    ("LOGIN", "login"),
    ("", ""),
], ids=["trim", "lowercase", "empty"])
def test_normalize(raw, expected):
    assert raw.strip().lower() == expected
