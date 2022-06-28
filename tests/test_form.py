from selene.support.shared import browser
from selene import have
import os
import demoqa_tests
from pathlib import Path



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

    browser.element('#subjectsInput').type('English').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../tests/котик.png'))

    browser.element('#currentAddress').type('Yekatetinburg')

    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    browser.element('#submit').click()

    #then
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
        'Subjects English'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[7].should(have.exact_text(
        'Hobbies Sports'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[8].should(have.exact_text(
        'Picture котик.png'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[9].should(have.exact_text(
        'Address Yekatetinburg'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr')[10].should(have.exact_text(
        'State and City Haryana Karnal'))





