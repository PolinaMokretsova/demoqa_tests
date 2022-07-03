from selene import command, have
from selene.core.entity import SeleneElement
from selene.support.shared import browser



def select_from_list(element: SeleneElement, /, *, option: str):
    browser.all('option').element_by(have.exact_text(option)).click()



def explicit_input(element: SeleneElement, /, *, option: str):
    element.perform(command.js.set_value(option)).click()