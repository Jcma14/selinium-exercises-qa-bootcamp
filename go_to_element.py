from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Find the Email field and fill it in
driver.find_element(By.ID, "email").send_keys("otroemail@email.com")

# Find the Password field and fill it in
driver.find_element(By.ID, "password").send_keys("email")

# Find login button, then click it
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Use the wait object until the user section is visible after logging in
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Find footer
element = driver.find_element(By.TAG_NAME, "footer")

# Scroll to the footer section
driver.execute_script("arguments[0].scrollIntoView();", element)

# Verify that the footer contains the string 'Around'
assert 'Around' in element.text

driver.quit()