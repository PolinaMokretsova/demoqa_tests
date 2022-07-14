from selene.support.shared import browser
from demoqa_tests.model import app


def test_submit_form():
    browser.open('/automation-practice-form')

    # when
    app.form.set_FirstName('Polina').set_LastName('Mokretsova').set_Email('Polina@polina.com')

    app.form.add_Gender('Female')

    app.form.add_Number('8123456789')

    app.form.set_birth_date('31 Jul 1980')

    app.form.add_Subjects('English', 'Maths')

    app.form.add_Hobbies('Sports')

    app.form.upload_Picture('котик.png')

    app.form.set_Address('Yekaterinburg')

    app.form.set_States('Haryana')

    app.form.set_Cities('Karnal')

    app.form.submit()

    # then
    app.results.should_Have_Exact_Texts('Student Name', 'Polina Mokretsova')
    app.results.should_Have_Exact_Texts('Student Email', 'Polina@polina.com')
    app.results.should_Have_Exact_Texts('Gender', 'Female')
    app.results.should_Have_Exact_Texts('Mobile', '8123456789')
    app.results.should_Have_Exact_Texts('Date of Birth', '14 July,2022')
    app.results.should_Have_Exact_Texts('Subjects', 'English, Maths')
    app.results.should_Have_Exact_Texts('Hobbies', 'Sports')
    app.results.should_Have_Exact_Texts('Picture', 'котик.png')
    app.results.should_Have_Exact_Texts('Address', 'Yekatetinburg')
    app.results.should_Have_Exact_Texts('State and City', 'Haryana Karnal')
