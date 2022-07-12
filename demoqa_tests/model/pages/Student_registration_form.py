from selene.support.shared import browser
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.resourse import resourse
from demoqa_tests.model.controls.tags_input_ import TagsInput


class StudentRegistrationForm:

    def set_FirstName(self, value):
        browser.element('#firstName').type('Polina')
        return self

    def set_LastName(self, value):
        browser.element('#lastName').type('Mokretsova')
        return self

    def set_Email(self, value):
        browser.element('#userEmail').type('Polina@polina.com')
        return self

    def set_birth_date(self, param):
        Date_Of_Birth = DatePicker(browser.element('#dateOfBirthInput'))
        Date_Of_Birth.explicit_input(option='31 Jul 1980')
        return self

    def submit(self):
        browser.element('#submit').click()

    def set_Address(self, param):
        browser.element('#currentAddress').type('Yekatetinburg')

    def upload_Picture(self, param):
        browser.element('#uploadPicture').send_keys(resourse('котик.png'))

    def add_Hobbies(self, param):
        Sports = '[for="hobbies-checkbox-1"]'
        browser.element(Sports).click()

    def add_Number(self, param):
        browser.element('#userNumber').type('8123456789')

    def add_Gender(self, param):
        Female = '[for=gender-radio-2]'
        browser.element(Female).click()

    def set_States(self, param):
        states = Dropdown(browser.element('#state'))
        states.select(option='Haryana')

    def set_Cities(self, param):
        city = Dropdown(browser.element('#city'))
        city.select(option='Karnal')

    def add_Subjects(self, *names):
        for name in names:
            TagsInput(browser.element('#subjectsInput')).add(name)
        return self
