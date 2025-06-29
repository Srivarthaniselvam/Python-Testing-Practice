from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert says:", alert.text)
alert.accept()
print("Alert accepted.")

time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

confirm_alert = driver.switch_to.alert
confirm_alert.dismiss()
print("Confirm alert dismissed.")

time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Hello from Selenium!")
prompt_alert.accept()
print("Prompt alert accepted with input.")

time.sleep(3)
driver.quit()
