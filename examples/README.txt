WAY2PYTHON PRACTICE KIT

Use Python 3.12 or newer. Unzip and open the kit folder in your terminal.
The dependency ranges allow a compatible setup; freeze your verified versions
into requirements-lock.txt before using the suite in CI.

SETUP (macOS/Linux)
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install -r requirements.txt
  python -m playwright install chromium

Windows PowerShell:
  py -m venv .venv
  .venv\Scripts\Activate.ps1
  python -m pip install -r requirements.txt
  python -m playwright install chromium

BROWSER TESTS
The Way2Python site must be running and Chrome installed for Selenium.
  python -m pytest test_playwright_lab.py --base-url http://localhost:8080/way2python
  python -m pytest test_selenium_lab.py

If your site uses another address, update --base-url for Playwright and set
WAY2PYTHON_URL for Selenium. In macOS/Linux:
  WAY2PYTHON_URL=http://localhost:8081/way2python python -m pytest test_selenium_lab.py
In PowerShell:
  $env:WAY2PYTHON_URL="http://localhost:8081/way2python"

API TESTS
In one terminal (no extra dependencies required by the server):
  python mock_api.py --port 8765
In another terminal using the same activated virtual environment:
  python -m pytest test_api_lab.py -q

The server binds to 127.0.0.1, stores records in memory, and has a fixed demo
token. It is a local exercise, not a production authentication service.
Stop with Ctrl+C. Records disappear on restart. Test users use unique emails.

API contract:
  GET /health: 200, {"status":"ok"}, no token required.
  Authorization: Bearer demo-token for /users.
  GET /users?limit=2: 200, {"items":[...],"total":N}; limit 1..100.
  POST /users: 201 with id, name, email.
  GET /users/<id>: 200 or 404.
  PATCH /users/<id>: 200, supports name/email updates, or 404.
  DELETE /users/<id>: 204 with empty body, or 404.
  Missing/invalid token: 401. Duplicate email: 409.
  Missing/invalid fields and unknown fields: 422. Malformed JSON: 400.
  Name: string, trimmed length 1..100.
  Email: simple local-lab shape validation, compared case-insensitively.

DATA ANALYSIS
  python analyze_results.py

LESSON SNIPPETS
Copy a lesson example into a separate file to explore it. Shell commands in
the website may use examples/ paths when run from the full site folder; the
downloaded kit keeps those same files at its root, so omit examples/ there.
Adaptation patterns are labeled separately from complete runnable examples.

REPORTS
  python -m pytest test_api_lab.py --junitxml=reports/api.xml
  python -m pytest test_playwright_lab.py --base-url http://localhost:8080/way2python --tracing retain-on-failure --screenshot only-on-failure

Keep actual credentials, tokens, and authenticated storage-state files out of
source control and reports. The demo values in this kit are public test data.
