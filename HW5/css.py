from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test():
    # Переход на страницу
    driver.get("http://uitestingplayground.com/classattr")

    def script():
        # Клик на синюю кнопку 
        search_input = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        search_input.click()
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                'Timed out waiting for PA creation ' +
                                'confirmation popup to appear.')
        alert.accept()
        sleep(5)

    #Запустить скрипт три раза
    for x in range(3):
        script()

    # Закрытие веб-драйвера
    driver.quit()

driver = webdriver.Chrome()
test()

driver = webdriver.Firefox()
test()

