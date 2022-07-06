from selene.core.entity import Element
from selene.support.shared import browser

class Table:

    @staticmethod
    def cells_of_row(index):
       return browser.element(
         '.modal-content .table'
      ).all('tbody tr')[index].all('td')

