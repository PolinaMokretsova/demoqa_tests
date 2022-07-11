
from selene import have
from selene.support.shared import browser
from demoqa_tests.model import app



def test_submit_form():
    browser.open('/automation-practice-form')

    #when
    app.form.setFirstName('Polina').setLastName('Mokretsova').setEmail('Polina@polina.com')

    app.form.addGender('Female')

    app.form.addNumber('8123456789')

    app.form.set_birth_date('31 Jul 1980')

    app.form.addSubjects('English', 'Maths')

    app.form.addHobbies('Sports')

    app.form.uploadPicture('котик.png')

    app.form.setAddress('Yekaterinburg')

    app.form.setStates('Haryana')

    app.form.setCities('Karnal')

    app.form.submit()

    # then
    app.results.should_Have_Exact_Texts('Student Name', 'Polina Mokretsova')
    app.results.should_Have_Exact_Texts('Student Email', 'Polina@polina.com')
    app.results.should_Have_Exact_Texts('Gender', 'Female')
    app.results.should_Have_Exact_Texts('Mobile', '8123456789')
    app.results.should_Have_Exact_Texts('Date of Birth', '11 July,2022')
    app.results.should_Have_Exact_Texts('Subjects', 'English, Maths')
    app.results.should_Have_Exact_Texts('Hobbies', 'Sports')
    app.results.should_Have_Exact_Texts('Picture', 'котик.png')
    app.results.should_Have_Exact_Texts('Address', 'Yekatetinburg')
    app.results.should_Have_Exact_Texts('State and City', 'Haryana Karnal')



