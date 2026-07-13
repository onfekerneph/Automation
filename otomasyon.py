from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://ornek-site.com")

# Giriş yap
driver.find_element(By.ID, "username").send_keys("test")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login").click()

# Reklam sayfasına git
driver.get("https://ornek-site.com/reklam")

# Reklamın bitmesini bekle
time.sleep(30)

# Ödülü al
driver.find_element(By.ID, "reward").click()

driver.quit()
