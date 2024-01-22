import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.implicitly_wait(30)
    driver.quit()



#Откройте сайт магазина
def test_internet_shop(driver):
    driver.get("https://www.saucedemo.com/")

    #Авторизуйтесь как пользователь
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    #Добавьте в корзину товары
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    #Перейдите в корзину.
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    #Нажмите Checkout.
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    #Заполните форму своими данными:
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Валентина")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Балашова")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("454003")

    #Нажмите кнопку Continue.
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    #Прочитайте со страницы итоговую стоимость
    element = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    assert element == 'Total: $58.29'

#Проверьте, что итоговая сумма равна $58.29
