
from selene import have, command
from selene.support.shared import browser
from demoqa_tests.controls import dropdown, datepicker
from demoqa_tests.controls.table import cells_of_row
from demoqa_tests.controls.resourse import resourse
from demoqa_tests.controls.tags_input_ import TagsInput


def test_submit_form():
    browser.open('/automation-practice-form')

    #when
    browser.element('#firstName').type('Polina')
    browser.element('#lastName').type('Mokretsova')
    browser.element('#userEmail').type('Polina@polina.com')

    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').type('8123456789')

    datepicker.explicit_input(browser.element('#dateOfBirthInput'), option= '31 Jul 1980')

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Eng', autocomplete='English')
    subjects.add('Maths')

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(resourse('котик.png'))

    browser.element('#currentAddress').type('Yekatetinburg')

    dropdown.select(browser.element('#state'), option='Haryana')
    dropdown.select(browser.element('#city'), option='Karnal')

    browser.element('#submit').click()

    # then
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    result = cells_of_row
    result(0).should(have.exact_texts('Student Name', 'Polina Mokretsova'))
    result(1).should(have.exact_texts('Student Email', 'Polina@polina.com'))
    result(2).should(have.exact_texts('Gender', 'Female'))
    result(3).should(have.exact_texts('Mobile', '8123456789'))
    result(4).should(have.exact_texts('Date of Birth', '05 July,2022'))
    result(5).should(have.exact_texts('Subjects', 'English, Maths'))
    result(6).should(have.exact_texts('Hobbies', 'Sports'))
    result(7).should(have.exact_texts('Picture', 'котик.png'))
    result(8).should(have.exact_texts('Address', 'Yekatetinburg'))
    result(9).should(have.exact_texts('State and City', 'Haryana Karnal'))



