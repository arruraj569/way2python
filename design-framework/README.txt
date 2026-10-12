WAY2PYTHON — DAILY SELENIUM FRAMEWORK

WHAT IT DOES
Three checks: valid login, rejected invalid login, and a profile update.
Each check gets a fresh browser. Page objects own UI operations, a profile
component owns a form, tests own assertions, and a yield fixture quits the
driver even when a check fails. Demo credentials belong only to this lab.

PREPARE
Install Python 3.12 or newer and Chrome. Keep the Way2Python site running at
http://localhost:8080/way2python/practice.html. Unzip the design-pattern kit,
then open a terminal inside its framework folder.

macOS / Linux:
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install -r requirements.txt
  python -m pytest test_daily_smoke.py -q

Windows PowerShell:
  py -m venv .venv
  .venv\Scripts\Activate.ps1
  python -m pip install -r requirements.txt
  python -m pytest test_daily_smoke.py -q

Expected when run successfully: 3 passed (duration varies).
Selenium Manager may require network access to obtain a matching driver.

OPTIONAL SETTINGS
The factory defaults to headless Chrome. To use installed Firefox:
  macOS / Linux: export WAY2PYTHON_BROWSER=firefox
  PowerShell: $env:WAY2PYTHON_BROWSER="firefox"

To use an alternate copy of the local site:
  macOS / Linux: export WAY2PYTHON_URL=http://localhost:8081/way2python
  PowerShell: $env:WAY2PYTHON_URL="http://localhost:8081/way2python"

READING ORDER
cases.py -> driver_factory.py -> conftest.py -> components.py -> pages.py
-> test_daily_smoke.py. Run from this folder so local imports resolve.

EXERCISE
Add another invalid login case and assert the rejection. Add a second profile
track with its exact visible label. Keep each test independent and use the
fixture for cleanup rather than storing a global driver.

VERIFICATION
Framework files were compiled; the local practice controls were checked in
the supported browser. This Python Selenium suite was not executed during
site generation. Run it locally to verify installed browser/driver behavior.
