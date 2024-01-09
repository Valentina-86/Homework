import pytest
from selenium import webdriver

from pg_test_forma import Forma
from test_calculyator import Calculaytor
from test_intrnet_magazin import Internet_shop


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_pr_forma(driver):
   
    pg_forma = Forma(driver) 
    pg_forma.send_keys()
    pg_forma.click()
    pg_forma.zip_code_field()
    pg_forma.other_fields()

def test_calculyator(driver):

    test_calculyator = Calculaytor(driver)
    test_calculyator.delay()
    test_calculyator.click()
    test_calculyator.sleep()
    test_calculyator.result_window()

def test_internet_magazin(driver):

    test_internet_magazin = Internet_shop(driver)
    test_internet_magazin.test_keys()
    test_internet_magazin.click()
    test_internet_magazin.cart_link()
    test_internet_magazin.checkout()
    test_internet_magazin.send_keys()
    test_internet_magazin.element()
    