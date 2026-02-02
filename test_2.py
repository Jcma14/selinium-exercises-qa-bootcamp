import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")

# Pauses execution for 5 seconds to allow the page to load properly
time.sleep(5)

# To find an element
driver.find_element(By.XPATH, ".//img")

#To find a group of elements
driver.find_elements(By.XPATH, ".//input")