import time
from selenium.webdriver.common.by import By


class Calculaytor:
        
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение 45 в поле с id="delay"
    def delay(self):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

    # Нажимаем на кнопки 7, +, 8, =
    def click(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "btn-outline-primary")
        elements.extend(self.driver.find_elements(By.CLASS_NAME, "btn-outline-success"))
        elements.extend(self.driver.find_elements(By.CLASS_NAME, "btn-outline-warning"))
        for element in elements:
            if element.text == '7':
                element.click()
        for element in elements:
            if element.text == '+':
                element.click()
        for element in elements:
            if element.text == '8':
                element.click()
        for element in elements:
            if element.text == '=':
                element.click()

    # Ждем 45 секунд
    def sleep(self):
        time.sleep(45)

    # Проверяем, что в окне отобразится результат 15
    def result_window(self):
        result_window = self.driver.find_element(By.CLASS_NAME, "screen")
        assert result_window.text == "15"

   