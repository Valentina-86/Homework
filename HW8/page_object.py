from selenium import webdriver

from pg_test_forma import Forma
from test_calculyator import Calculaytor


def test_forma_pg():
    browser = webdriver.Chrome()

    pg_forma = Forma(browser) 
    pg_forma.send_keys()
    pg_forma.click()
    pg_forma.zip_code_field()
    pg_forma.other_fields()

    browser.quit()

def test_calculyator():
    browser = webdriver.Chrome()

    test_calculyator = Calculaytor(browser)
    test_calculyator.delay()
    test_calculyator.click()
    test_calculyator.sleep()
    test_calculyator.result_window()
    
    browser.quit()