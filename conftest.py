import pytest
import pytest_html
from utils.browser import get_driver
from utils.screenshot import capture_screenshot
from config.env_config import ENVIRONMENTS


# --------------------------
# CLI OPTIONS
# --------------------------
def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome | firefox | edge"
    )

    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment: qa | stage | prod"
    )


# --------------------------
# DRIVER FIXTURE
# --------------------------
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()


# --------------------------
# ENV FIXTURE
# --------------------------
@pytest.fixture(scope="session")
def base_url(request):

    env = request.config.getoption("--env").lower()

    if env not in ENVIRONMENTS:
        raise ValueError(f"Invalid environment: {env}")

    return ENVIRONMENTS[env]["base_url"]


# --------------------------
# SCREENSHOT HOOK
# --------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            path = capture_screenshot(driver, item.name)

            html = f'<div><img src="{path}" width="300" height="200" onclick="window.open(this.src)" align="right"/></div>'
            extras.append(pytest_html.extras.html(html))

    report.extras = extras
