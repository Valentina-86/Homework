from selenium.webdriver.common.by import By


class Internet_shop:

    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def authorize(self, user_name:str, password:str):
        """
        Выполняет авторизацию пользователя на сайте.

        Побочные эффекты:
        Вводит имя пользователя и пароль в соответствующие поля и нажимает кнопку входа.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def click_goods(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")
        """
        Добавляет выбранные товары в корзину покупок.

        Побочные эффекты:
        Переходит на страницу с товарами и добавляет указанные товары в корзину.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def to_cart(self):
        """
        Переходит в корзину и начинает процесс оформления заказа.

        Побочные эффекты:
        Переходит в корзину и нажимает кнопку оформления заказа (Checkout).
        """
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def send_keys(self, first_name:str, last_name:str, index:str):
        """
        Заполняет форму оформления заказа данными пользователя.

        Побочные эффекты:
        Заполняет поля формы данными и нажимает кнопку продолжения оформления заказа (Continue).
        """
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(index)
        
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def element(self) -> str:
        """
        Возвращает элемент, содержащий итоговую стоимость заказа.

        Возвращает:
        WebElement: Элемент, содержащий текст с итоговой стоимостью заказа.
        """
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        
