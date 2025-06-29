from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()

login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

time.sleep(2)

dropdown_element = driver.find_element(By.ID, "dropdown")

select = Select(dropdown_element)

all_options = select.options
print("Available dropdown options:")
for option in all_options:
    print(" -", option.text)

select.select_by_visible_text("Option 2")

time.sleep(3)
driver.quit()
