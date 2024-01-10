import pytest
from selenium import webdriver

from pg_forma import Forma
from pg_calculyator import Calculaytor
from pg_intrnet_magazin import Internet_shop


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_pg_forma(driver):
   
    pg_forma = Forma(driver) 
    pg_forma.send_keys("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")

    zip_code_field = pg_forma.zip_code_field()
    assert "alert-danger" in zip_code_field.get_attribute("class")

    other_fields = pg_forma.other_fields()
    for field in other_fields:
        assert "alert-success" in field.get_attribute("class")

def test_calculyator(driver):

    test_calculyator = Calculaytor(driver)
    test_calculyator.delay("45")
    test_calculyator.click_buttons('7', '+', '8', '=')
    test_calculyator.sleep(45)
    result_window = test_calculyator.result_window()

    assert result_window.text == "15"

def test_internet_magazin(driver):

    test_internet_magazin = Internet_shop(driver)
    test_internet_magazin.authorize('standard_user', 'secret_sauce')
    test_internet_magazin.click_goods()
    test_internet_magazin.to_cart()
    test_internet_magazin.click_checkout()
    test_internet_magazin.send_keys("Валентина", "Балашова", "454003")
    element = test_internet_magazin.element()

    assert element == 'Total: $58.29'
    