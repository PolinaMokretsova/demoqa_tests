from selene import command, have
from selene.core.entity import SeleneElement, Element
from selene.support.shared import browser

class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_from_list(self, /, *, option: str):
     self.browser.all('option').element_by(have.exact_text(option)).click()


    def explicit_input(self, /, *, option: str):
      self.element.perform(command.js.set_value(option)).click()