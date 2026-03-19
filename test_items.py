from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_basket(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".add-to-basket > button.btn")
    assert button is not None, "Basket button hasn't been found"