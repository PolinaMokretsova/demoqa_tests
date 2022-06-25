import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse="true")
def browser_config():
    browser.config.base_url= 'https://demoqa.com'
    browser.config.browser_name= 'chrome'
    browser.config.window_width = 390
    browser.config._window_height = 850


