
from selenium.webdriver.common.by import By

class Internet_shop:

    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def test_keys(self):
        #Авторизуйтесь как пользователь
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def click(self):
        #Добавьте в корзину товары
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def cart_link(self):
        #Перейдите в корзину.
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    def checkout(self):
        #Нажмите Checkout.
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def send_keys(self):
        #Заполните форму своими данными:
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Валентина")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Балашова")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("454003")
        #Нажмите кнопку Continue.
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def element(self):
        #Прочитайте со страницы итоговую стоимость
        element = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        #Проверьте, что итоговая сумма равна $58.29
        assert element == 'Total: $58.29'
