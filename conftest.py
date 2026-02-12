import pytest
import pytest_html
from utils.browser import get_driver
from utils.screenshot import capture_screenshot

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome | firefox | edge"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            path = capture_screenshot(driver, item.name)

            if path:
                html = f'<div><img src="{path}" width="300" height="200" onclick="window.open(this.src)" align="right"/></div>'
                extras.append(pytest_html.extras.html(html))

    report.extras = extras

