import pytest
from cases import CaseRepository
from pages import PracticePage

@pytest.mark.parametrize("name", ["valid", "invalid"])
def test_login_outcome(driver, name):
    case = CaseRepository().get(name)
    page = PracticePage(driver)
    page.sign_in(case.email, case.password)
    assert page.login_status(case.expected) == case.expected

def test_profile_update(driver):
    page = PracticePage(driver)
    page.profile.save("Mira", "selenium")
    expected = "Profile saved: Mira · Selenium · updates off"
    assert page.profile.status(expected) == expected
