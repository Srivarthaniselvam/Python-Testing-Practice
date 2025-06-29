from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
time.sleep(3)

driver.refresh()
time.sleep(3)

driver.quit()
