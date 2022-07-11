from selene.support.shared import browser
from typing import Optional

from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.resourse import resourse
from demoqa_tests.model.controls.tags_input_ import TagsInput


class StudentRegistrationForm:

    def setFirstName(self, value):
        browser.element('#firstName').type('Polina')
        return self

    def setLastName(self, value):
        browser.element('#lastName').type('Mokretsova')
        return self


    def setEmail(self,value):
        browser.element('#userEmail').type('Polina@polina.com')
        return self


    def set_birth_date(self, param):
        DateOfBirth = DatePicker(browser.element('#dateOfBirthInput'))
        DateOfBirth.explicit_input(option='31 Jul 1980')
        return self

    def submit(self):
        browser.element('#submit').click()

    def setAddress(self, param):
        browser.element('#currentAddress').type('Yekatetinburg')

    def uploadPicture(self, param):
        browser.element('#uploadPicture').send_keys(resourse('котик.png'))

    def addHobbies(self, param):
        Sports = '[for="hobbies-checkbox-1"]'
        browser.element(Sports).click()

    def addNumber(self, param):
        browser.element('#userNumber').type('8123456789')

    def addGender(self, param):
        Female = '[for=gender-radio-2]'
        browser.element(Female).click()

    def setStates(self, param):
        states = Dropdown(browser.element('#state'))
        states.select(option='Haryana')

    def setCities(self, param):
        city = Dropdown(browser.element('#city'))
        city.select(option='Karnal')

    def addSubjects(self, *names, autocomplete: Optional[str] = None):
        for name in names:
            TagsInput('subjectsInput').add(name)
        return self
     #subjects = TagsInput(browser.element('#subjectsInput'))
    # subjects.add('Eng', autocomplete='English').add('Maths')

