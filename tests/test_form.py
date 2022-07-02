from typing import Optional
from xml.etree.ElementTree import Element

from selene.core.entity import SeleneElement
from selene.support.shared import browser
from selene import have
from selene.support.shared import browser
from demoqa_tests.controls import dropdown
from demoqa_tests.controls.resourse import resourse
#from demoqa_tests.controls import tags_input
from demoqa_tests.controls.tags_input_ import TagsInput


def test_submit_form():
    browser.open('/automation-practice-form')

    #when
    browser.element('#firstName').type('Polina')
    browser.element('#lastName').type('Mokretsova')
    browser.element('#userEmail').type('Polina@polina.com')

    browser.element('[for="gender-radio-2"]').click()

    browser.element('#userNumber').type('8123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1999"]').click()
    browser.element('[value="6"]').click()
    browser.element('div[aria-label="Choose Monday, July 26th, 1999"]').click()

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
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[1].should(have.exact_text(
        'Student Name Polina Mokretsova'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[2].should(have.exact_text(
        'Student Email Polina@polina.com'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[3].should(have.exact_text(
        'Gender Female'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[4].should(have.exact_text(
        'Mobile 8123456789'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[5].should(have.exact_text(
        'Date of Birth 26 July,1999'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[6].should(have.exact_text(
        'Subjects English, Maths'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[7].should(have.exact_text(
        'Hobbies Sports'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[8].should(have.exact_text(
        'Picture котик.png'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[9].should(have.exact_text(
        'Address Yekatetinburg'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[10].should(have.exact_text(
        'State and City Haryana Karnal'))


