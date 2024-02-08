import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Calculaytor:
        
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
    def delay(self, time:str):
        """
        Устанавливает значение задержки в поле ввода.

        Параметры:
        time (int или str): 45 в поле id='delay'.
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(time)
        
    def click_buttons(self, button1:str, button2:str, button3:str, button4:str):
        """
        Нажимает на последовательность кнопок на калькуляторе.

        Параметры:
        button1 (str): 7.
        button2 (str): +.
        button3 (str): 8.
        button4 (str): =.

        Побочные эффекты:
        Нажимает на кнопки на веб-странице и ожидает, пока результат не будет отображен.
        """
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

        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))

    
    def result_window(self) -> int:
        """
        Получает элемент окна с результатом вычислений.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen")
        

   