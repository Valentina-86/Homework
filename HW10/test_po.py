import pytest
from selenium import webdriver
import allure

from forma import Forma
from calculyator import Calculaytor
from internet import Internet_shop


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.story('Заполнение формы')
@allure.feature('Send')
@allure.title('Заполнение формы')
@allure.description('Заполнить форму своими данными')
@allure.severity('BLOCKER')
@allure.epic('PageObject')
def test_pg_forma(driver):
    pg_forma = Forma(driver)
    with allure.step('Заполнить поля формы своими данными'): 
        pg_forma.send_keys("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")

    with allure.step('Проверить, что поле Zip code красным цветом'): 
        zip_code_field = pg_forma.zip_code_field()
        assert "alert-danger" in zip_code_field.get_attribute("class")

    with allure.step('Проверить, что остальные поля отмечены зеленым цветом'):
        other_fields = pg_forma.other_fields()
        for field in other_fields:
            assert "alert-success" in field.get_attribute("class")

@allure.story('Калькулятор')
@allure.feature('Click')
@allure.title('Работа калькулятора')
@allure.description('Нажать на кнопки 7 + 8 =')
@allure.severity('BLOCKER')
@allure.epic('PageObject')
def test_calculyator(driver):

    test_calculyator = Calculaytor(driver)
    with allure.step('Подождать 45 сек'):
        test_calculyator.delay("45")

    with allure.step('Нажать на кнопки 7 + 8 ='):
        test_calculyator.click_buttons('7', '+', '8', '=')

    with allure.step('Подождать 45 сек'):
        result_window = test_calculyator.result_window()

    with allure.step('Проверить,  что отобразилось число 15'):
        assert result_window.text == "15"

@allure.story('Интернет-магазин')
@allure.feature('Internet')
@allure.title('Интернет-магазин')
@allure.description('Залогиниться в интернет-магазине и заполнить все поля')
@allure.severity('BLOCKER')
@allure.epic('PageObject')
def test_internet_magazin(driver):

    test_internet_magazin = Internet_shop(driver)

    with allure.step('Ввести логин и пароль'):
        test_internet_magazin.authorize('standard_user', 'secret_sauce')
    
    with allure.step('Нажать войти'):
        test_internet_magazin.click_goods()

    with allure.step('Перейти в корзину'):
        test_internet_magazin.to_cart()

    with allure.step('Заполнить форму заказа своими данными'):
        test_internet_magazin.send_keys("Валентина", "Балашова", "454003")
        element = test_internet_magazin.element()

    with allure.step('Проверить, что на экране отобразилась сумма 58,29'):
        assert element == 'Total: $58.29'
    