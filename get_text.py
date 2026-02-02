from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# This object will be used for all explicit waits
wait = WebDriverWait(driver, 10)

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Use the wait object until the email field is present, then enter it
wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("otroemail@email.com")

# Use the wait object until the password field is present, then enter it
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("email")

# Use the wait object until the login button is clickable, then click it
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".auth-form__button"))).click()

# Use the wait object until the user section is visible after logging in
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__user")))

# Use the wait object to get the logout button and verify its text is 'Log out'
logout_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header__logout"))).text
assert logout_text.strip() == 'Log out', f"Expected 'Log out', got '{logout_text}'"

driver.quit()




