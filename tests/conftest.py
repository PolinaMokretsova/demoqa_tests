import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 500
    browser.config._window_height = 1000
