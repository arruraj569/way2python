def can_register(age):
    return age >= 18

def test_registration_boundary():
    assert can_register(17) is False
    assert can_register(18) is True
    assert can_register(19) is True
