from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#award'))).get_dom_attribute("src")
print(element)

driver.quit()