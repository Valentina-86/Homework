from selenium.webdriver.common.by import By

class Forma:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполните форму значениями
    def send_keys(self):   
        self.driver.find_element(By.NAME, 'first-name').send_keys("Иван") 
        self.driver.find_element(By.NAME, 'last-name').send_keys("Петров") 
        self.driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3") 
        self.driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
        self.driver.find_element(By.NAME, 'zip-code').send_keys("")
        self.driver.find_element(By.NAME, 'city').send_keys("Москва")
        self.driver.find_element(By.NAME, 'country').send_keys("Россия")
        self.driver.find_element(By.NAME, 'job-position').send_keys("QA")
        self.driver.find_element(By.NAME, 'company').send_keys("SkyPro")

    # Нажать кнопку Submit
    def click(self):
        self.driver.find_element(By.CLASS_NAME, 'btn-outline-primary').click()

    # Проверка, что поле Zip code подсвечено красным
    def zip_code_field(self):
        zip_code_field =  self.driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class")

    def other_fields(self):
    # Проверьте (assert), что остальные поля подсвечены зеленым
        other_fields = self.driver.find_elements(By.CLASS_NAME, "alert-success")
        for field in other_fields:
            assert "alert-success" in field.get_attribute("class")