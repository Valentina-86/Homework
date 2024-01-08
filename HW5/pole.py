from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    #Введите в поле текст `1000`
    search_input = driver.find_element(By.CSS_SELECTOR, "[type='number']")
    search_input.send_keys(1000)
    sleep(2)

    #Очистите это поле (метод `clear`).
    search_input.clear()
    sleep(2)

    #Введите в это же поле текст `999`
    search_input = driver.find_element(By.CSS_SELECTOR, "[type='number']")
    search_input.send_keys(999)
    sleep(5)

    # Закрытие веб-драйвера
    driver.quit()


driver = webdriver.Chrome()
test()

driver = webdriver.Firefox()
test()

