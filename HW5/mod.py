from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
        # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(5)

    # В модальном окне нажмите на кнопку Сlose 
    search_input = driver.find_element(By.CLASS_NAME, "modal-footer").click()

    sleep(5)

    # Закрытие веб-драйвера
    driver.quit()

driver = webdriver.Chrome()
test()

driver = webdriver.Firefox()
test()

