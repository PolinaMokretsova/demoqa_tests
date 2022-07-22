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
    app.results.should_Have_Exact_Texts(0, 1, 'Polina Mokretsova')
    app.results.should_Have_Exact_Texts(1, 1, 'Polina@polina.com')
    app.results.should_Have_Exact_Texts(2, 1, 'Female')
    app.results.should_Have_Exact_Texts(3, 1, '8123456789')
    app.results.should_Have_Exact_Texts(4, 1, '22 July,2022')
    app.results.should_Have_Exact_Texts(5, 1, 'English, Maths')
    app.results.should_Have_Exact_Texts(6, 1, 'Sports')
    app.results.should_Have_Exact_Texts(7, 1, 'котик.png')
    app.results.should_Have_Exact_Texts(8, 1, 'Yekaterinburg')
    app.results.should_Have_Exact_Texts(9, 1, 'Haryana Karnal')
