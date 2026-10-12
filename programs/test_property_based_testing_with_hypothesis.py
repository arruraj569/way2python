from hypothesis import given, strategies as st
def normalize(text):
    return text.strip().lower()

@given(st.text())
def test_normalize_is_idempotent(text):
    assert normalize(normalize(text)) == normalize(text)
