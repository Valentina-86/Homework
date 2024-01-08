from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def test():
    # Переход на страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Клик на кнопку "Add Element" пять раз
    for i in range(5):
        add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))
        add_button.click()
        sleep(1)

    # Сбор списка кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    sleep(5)

    # Вывод размера списка на экран
    print(len(delete_buttons))

    # Закрытие веб-драйвера
    driver.quit()

driver = webdriver.Chrome()
test()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
test()

