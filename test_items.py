import time
from selenium.webdriver.common.by import By

base_link = "http://selenium1py.pythonanywhere.com"
second_link = "catalogue/coders-at-work_207"


class TestItems:
    def test_check_different_interface_languages(self, browser, lang):
        browser.get(f"{base_link}/{lang}/{second_link}")
        element = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket").text
        assert 'Añadir al carrito' == element or 'Ajouter au panier' == element
        time.sleep(5)
