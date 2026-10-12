def normalized_name(value):
    return value.strip().lower()

def test_normalized_name():
    actual = normalized_name("  LOGIN  ")
    assert actual == "login"

def test_empty_name():
    assert normalized_name("   ") == ""
