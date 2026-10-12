import pytest
@pytest.mark.parametrize("value, expected", [(1, 1), (2, 4), (3, 9)], ids=["one", "two", "three"])
def test_square(value, expected):
    assert value * value == expected

def test_empty_collection():
    assert sum([]) == 0
