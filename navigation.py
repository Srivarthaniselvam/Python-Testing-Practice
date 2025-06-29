from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://www.bing.com")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.quit()
