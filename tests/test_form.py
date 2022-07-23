from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from demoqa_tests.model import app
import allure
from demoqa_tests.utils import attach
from selenium import webdriver


def test_submit_form():
    options= Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    browser.open('/automation-practice-form')

    # when
    with allure.step("set firstname, lastname, email"):
        app.form.set_FirstName('Polina').set_LastName('Mokretsova').set_Email('Polina@polina.com')

    with allure.step("add gender"):
        app.form.add_Gender('Female')

    with allure.step("add number"):
        app.form.add_Number('8123456789')

    with allure.step("set birthday"):
        app.form.set_birth_date('31 Jul 1980')

    with allure.step("add subjects"):
        app.form.add_Subjects('English', 'Maths')

    with allure.step("add hobbies"):
        app.form.add_Hobbies('Sports')

   # with allure.step("upload picture"):
        #app.form.upload_Picture('котик.png')

    with allure.step("set address"):
        app.form.set_Address('Yekaterinburg')

    with allure.step("set states"):
        app.form.set_States('NCR')

    with allure.step("set cities"):
        app.form.set_Cities('Delhi')

    with allure.step("submit"):
        app.form.submit()

    # then
    with allure.step("fill form"):
        app.results.should_Have_Exact_Texts(0, 1, 'Polina Mokretsova')
        app.results.should_Have_Exact_Texts(1, 1, 'Polina@polina.com')
        app.results.should_Have_Exact_Texts(2, 1, 'Female')
        app.results.should_Have_Exact_Texts(3, 1, '8123456789')
        app.results.should_Have_Exact_Texts(4, 1, '23 July,2022')
        app.results.should_Have_Exact_Texts(5, 1, 'English, Maths')
        app.results.should_Have_Exact_Texts(6, 1, 'Sports')
        #app.results.should_Have_Exact_Texts(7, 1, 'котик.png')
        app.results.should_Have_Exact_Texts(8, 1, 'Yekaterinburg')
        app.results.should_Have_Exact_Texts(9, 1, 'NCR Delhi')

    attach.add_html(browser)
    attach.add_screenshots(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
