import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Find the Email field and fill it in
driver.find_element(By.ID, "email").send_keys("otroemail@email.com")

# Find the Password field and fill it in
driver.find_element(By.ID, "password").send_keys("email")

time.sleep(2)

# Find the Log In button and click it
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Add an explicit wait for the page to load
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user"))
)

# Check that the current URL is 'https://around-v1.nm.tripleten-services.com/'
assert driver.current_url == 'https://around-v1.nm.tripleten-services.com/'

driver.quit()





