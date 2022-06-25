from selene.support.shared import browser
from selene import be, have, command
import pytest


def test_submit_form():
   browser.open('/automation-practice-form')


   browser.element('#firstName').should(be.blank).type('Polina')
   browser.element('#lastName').should(be.blank).type('Mokretsova')
   browser.element('#userEmail').should(be.blank).type('Polina@polina.com')
   browser.element('[for="gender-radio-2"]').click()
   browser.element('#userNumber').should(be.blank).type('8123456789')
   browser.element('#dateOfBirthInput').set_value('25 jun 1990')
   browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
   browser.element('[for="hobbies-checkbox-1"]').click()
   browser.element('#uploadPicture').type("/Users/mokretsova/PycharmProjects/demoqa_tests/tests/котик.png")
   browser.element('#currentAddress').should(be.blank).type('Yekatetinburg')
   browser.element('#react-select-3-input').type('Haryana').press_enter()
   browser.element('#react-select-4-input').type('Karnal').press_enter()
   browser.element('#submit').click()


