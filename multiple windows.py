from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
driver.close()

driver.switch_to.window(windows[0])
print(driver.title)

driver.quit()
