from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
    def script():
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Клик на синюю кнопку 
        search_input = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
        search_input.click()
        sleep(3)

    #Запустить скрипт три раза
    for x in range(3):
        script()

    # Закрытие веб-драйвера
    driver.quit()

driver = webdriver.Chrome()
test()

driver = webdriver.Firefox()
test()

