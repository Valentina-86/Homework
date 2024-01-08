from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/login")

    #В поле username введите значение tomsmith
    #$$("[name='username']")
    search_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    search_input.send_keys('tomsmith')

    #В поле password введите значение SuperSecretPassword!
    #$$("[name='password']")
    search_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    search_input.send_keys('SuperSecretPassword!')

    #Нажмите кнопку Login
    search_input = driver.find_element(By.CLASS_NAME,"radius").click()

    sleep(3)

    # Закрытие веб-драйвера
    driver.quit()

driver = webdriver.Chrome()
test()

driver = webdriver.Firefox()
test()