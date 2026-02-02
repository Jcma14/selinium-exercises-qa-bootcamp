from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

driver.implicitly_wait(10)
# Log in
driver.find_element(By.ID, "email").send_keys("otroemail@email.com")
driver.find_element(By.ID, "password").send_keys("email")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()
# Add an explicit wait for the page to load
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "places__list"))
)
# Find the card and scroll it into view
element = driver.find_element(By.CSS_SELECTOR, ".places__item")
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.quit()
