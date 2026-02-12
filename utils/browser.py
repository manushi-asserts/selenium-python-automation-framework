from selenium import webdriver

def get_driver(browser):

    browser = browser.lower()

    try:
        if browser == "chrome":
            driver = webdriver.Chrome()

        elif browser == "firefox":
            driver = webdriver.Firefox()

        elif browser == "edge":
            driver = webdriver.Edge()

        else:
            raise ValueError("Unsupported browser")

    except Exception:
        print(f"Browser '{browser}' not available → launching Chrome instead")
        driver = webdriver.Chrome()

    driver.maximize_window()
    return driver
