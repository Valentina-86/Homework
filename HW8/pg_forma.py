from selenium.webdriver.common.by import By

class Forma:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполните форму значениями
    def send_keys(self, first_name, last_name, address, e_mail, phone, zip_code, city, country, job_position, company):   
        self.driver.find_element(By.NAME, 'first-name').send_keys(first_name) 
        self.driver.find_element(By.NAME, 'last-name').send_keys(last_name) 
        self.driver.find_element(By.NAME, 'address').send_keys(address) 
        self.driver.find_element(By.NAME, 'e-mail').send_keys(e_mail)
        self.driver.find_element(By.NAME, 'phone').send_keys(phone)
        self.driver.find_element(By.NAME, 'zip-code').send_keys(zip_code)
        self.driver.find_element(By.NAME, 'city').send_keys(city)
        self.driver.find_element(By.NAME, 'country').send_keys(country)
        self.driver.find_element(By.NAME, 'job-position').send_keys(job_position)
        self.driver.find_element(By.NAME, 'company').send_keys(company)

        # Нажать кнопку Submit
        self.driver.find_element(By.CLASS_NAME, 'btn-outline-primary').click()

    # Проверка, что поле Zip code подсвечено красным
    def zip_code_field(self):
        return  self.driver.find_element(By.ID, "zip-code")
        

    def other_fields(self):
    # Проверьте (assert), что остальные поля подсвечены зеленым
        return self.driver.find_elements(By.CLASS_NAME, "alert-success")
        