
from selenium.webdriver.common.by import By

class Internet_shop:

    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def authorize(self, user_name, password):
        """
            Авторизоваться как пользователь
        """
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def click_goods(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        """
            Добавить в корзину товары
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def to_cart(self):
        """
            Перейти в корзину.
        """
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        """
            Нажать Checkout.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def send_keys(self, first_name, last_name, index):
        """
            Заполнить форму своими данными
        """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(index)
        
        """
            Нажать кнопку Continue
        """
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def element(self):
        """
            Прочитать на странице итоговую стоимость
        """
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        
