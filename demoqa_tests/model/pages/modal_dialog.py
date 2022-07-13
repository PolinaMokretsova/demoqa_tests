
from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls.table import Table


class ModalDialog:

    def __init__(self):
        self.element=browser.element('.modal-content')
        self.table= Table(self.element.element('.table'))

    def should_Have_Exact_Texts(self, *values):
        self.table.cells_of_row(0).should(have.exact_texts('Student Name', 'Polina Mokretsova'))
        self.table.cells_of_row(1).should(have.exact_texts('Student Email', 'Polina@polina.com'))
        self.table.cells_of_row(2).should(have.exact_texts('Gender', 'Female'))
        self.table.cells_of_row(3).should(have.exact_texts('Mobile', '8123456789'))
        self.table.cells_of_row(4).should(have.exact_texts('Date of Birth', '13 July,2022'))
        self.table.cells_of_row(5).should(have.exact_texts('Subjects', 'English, Maths'))
        self.table.cells_of_row(6).should(have.exact_texts('Hobbies', 'Sports'))
        self.table.cells_of_row(7).should(have.exact_texts('Picture', 'котик.png'))
        self.table.cells_of_row(8).should(have.exact_texts('Address', 'Yekatetinburg'))
        self.table.cells_of_row(9).should(have.exact_texts('State and City', 'Haryana Karnal'))

