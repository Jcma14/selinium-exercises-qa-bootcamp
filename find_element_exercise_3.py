from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(5)

# Find elements
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")
#Test the placeholder attribute for each element
assert email.get_attribute('placeholder') == 'Email', f"Expected 'Email', but got '{email.get_attribute('placeholder')}'"
assert password.get_attribute('placeholder') == 'Password', f"Expected 'Password', but got '{password.get_attribute('placeholder')}'"
print("Login Successful")

driver.quit()





