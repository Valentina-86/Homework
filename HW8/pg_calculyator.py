import time
from selenium.webdriver.common.by import By


class Calculaytor:
        
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение 45 в поле с id="delay"
    def delay(self, time):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(time)

    # Нажимаем на кнопки 7, +, 8, =
    def click_buttons(self, button1, button2, button3, button4):
        elements = self.driver.find_elements(By.CLASS_NAME, "btn-outline-primary")
        elements.extend(self.driver.find_elements(By.CLASS_NAME, "btn-outline-success"))
        elements.extend(self.driver.find_elements(By.CLASS_NAME, "btn-outline-warning"))
        for element in elements:
            if element.text == button1:
                element.click()
        for element in elements:
            if element.text == button2:
                element.click()
        for element in elements:
            if element.text == button3:
                element.click()
        for element in elements:
            if element.text == button4:
                element.click()

    # Ждем 45 секунд
    def sleep(self, sleep):
        time.sleep(sleep)

    # Проверяем, что в окне отобразится результат 15
    def result_window(self):
        return self.driver.find_element(By.CLASS_NAME, "screen")
        

   