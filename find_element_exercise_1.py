import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

# fine title of element
title_element = driver.find_element(By.CSS_SELECTOR, ".auth-form__title")
# find and print the line with text
print("Login form title:", title_element.text)
# Close browser
driver.quit()