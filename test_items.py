import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_btn = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_btn, "Button is not present"

