import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Find button and click on it
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

time.sleep(2)

driver.quit()




