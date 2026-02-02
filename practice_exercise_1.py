from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
    EC.visibility_of_element_located((By.CLASS_NAME, "header__user"))
)

# Click on the profile photo
driver.find_element(By.CSS_SELECTOR, ".profile__image").click()

# Insert the photo link into the Link field using the avatar_url variable
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Save the new photo
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Save']").click()

# Wait for the profile photo to load
WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"), 'style', avatar_url))

# Save the value of the style attribute for the profile photo element into the variable style
style = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute('style')

# Verify that style contains the profile photo URL
assert avatar_url in style

driver.quit()