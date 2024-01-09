from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(30)

#Откройте сайт магазина
driver.get("https://www.saucedemo.com/")

#Авторизуйтесь как пользователь
element = driver.find_element(By.CSS_SELECTOR, "#user-name")
element.send_keys("standard_user")
element = driver.find_element(By.CSS_SELECTOR, "#password")
element.send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

#Добавьте в корзину товары
element = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
element = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
element = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

#Перейдите в корзину.
element = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

#Нажмите Checkout.
element = driver.find_element(By.CSS_SELECTOR, "#checkout").click()

#Заполните форму своими данными:
element = driver.find_element(By.CSS_SELECTOR, "#first-name")
element.send_keys("Валентина")
element = driver.find_element(By.CSS_SELECTOR, "#last-name")
element.send_keys("Балашова")
element = driver.find_element(By.CSS_SELECTOR, "#postal-code")
element.send_keys("454003")

#Нажмите кнопку Continue.
element = driver.find_element(By.CSS_SELECTOR, "#continue").click()

#Прочитайте со страницы итоговую стоимость
element = driver.find_element(By.CLASS_NAME, "summary_total_label").text

#Закройте браузер.
driver.quit()

#Проверьте, что итоговая сумма равна $58.29
print(element)