
from selene import have
from selene.support.shared import browser
from demoqa_tests.controls.datepicker import  DatePicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.resourse import resourse
from demoqa_tests.controls.tags_input_ import TagsInput


def test_submit_form():
    browser.open('/automation-practice-form')

    #when
    browser.element('#firstName').type('Polina')
    browser.element('#lastName').type('Mokretsova')
    browser.element('#userEmail').type('Polina@polina.com')

    gender_female = '[for=gender-radio-2]'
    browser.element(gender_female).click()

    browser.element('#userNumber').type('8123456789')

    Date_Of_Birth = DatePicker(browser.element('#dateOfBirthInput'))
    Date_Of_Birth.explicit_input(option= '31 Jul 1980')

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Eng', autocomplete='English')
    subjects.add('Maths')


    Hobbie_sports = '[for="hobbies-checkbox-1"]'
    browser.element(Hobbie_sports).click()

    browser.element('#uploadPicture').send_keys(resourse('котик.png'))

    browser.element('#currentAddress').type('Yekatetinburg')

    states = Dropdown(browser.element('#state'))
    states.select(option='Haryana')

    city = Dropdown(browser.element('#city'))
    city.select(option='Karnal')

    browser.element('#submit').click()

    # then
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    result = Table(browser.element('.modal-content .table'))
    result.cells_of_row(0).should(have.exact_texts('Student Name', 'Polina Mokretsova'))
    result.cells_of_row(1).should(have.exact_texts('Student Email', 'Polina@polina.com'))
    result.cells_of_row(2).should(have.exact_texts('Gender', 'Female'))
    result.cells_of_row(3).should(have.exact_texts('Mobile', '8123456789'))
    result.cells_of_row(4).should(have.exact_texts('Date of Birth', '12 July,2022'))
    result.cells_of_row(5).should(have.exact_texts('Subjects', 'English, Maths'))
    result.cells_of_row(6).should(have.exact_texts('Hobbies', 'Sports'))
    result.cells_of_row(7).should(have.exact_texts('Picture', 'котик.png'))
    result.cells_of_row(8).should(have.exact_texts('Address', 'Yekatetinburg'))
    result.cells_of_row(9).should(have.exact_texts('State and City', 'Haryana Karnal'))



