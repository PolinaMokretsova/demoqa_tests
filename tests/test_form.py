from selene.support.shared import browser
from selene import have
import os




def test_submit_form():
    browser.open('/automation-practice-form')


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


    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('[class="table table-dark table-striped table-bordered table-hover"] tr').should(have.texts(
      'Label Values'))
      #'Student Name Polina Mokretsova',
    #  'Student Email Polina@polina.com',
    #  'Gender Female', 'Mobile 8123456789',
     # 'Date of Birth 26 July,1999',
    #  'Subjects English',
     # 'Hobbies Sports',
     # 'Picture котик.png',
   #   'Address Yekatetinburg',
    #  'State and City Haryana Karnal'
 #  ))


