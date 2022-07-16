
from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls.table import Table


class ModalDialog:

    def __init__(self):
        self.element=browser.element('.modal-content')
        self.table= Table(self.element.element('.table'))

    def should_Have_Exact_Texts(self, *values):
        self.table.cells_of_row(0).should(have.exact_texts(*values))
        self.table.cells_of_row(1).should(have.exact_texts(*values))
        self.table.cells_of_row(2).should(have.exact_texts(*values))
        self.table.cells_of_row(3).should(have.exact_texts(*values))
        self.table.cells_of_row(4).should(have.exact_texts(*values))
        self.table.cells_of_row(5).should(have.exact_texts(*values))
        self.table.cells_of_row(6).should(have.exact_texts(*values))
        self.table.cells_of_row(7).should(have.exact_texts(*values))
        self.table.cells_of_row(8).should(have.exact_texts(*values))
        self.table.cells_of_row(9).should(have.exact_texts(*values))

