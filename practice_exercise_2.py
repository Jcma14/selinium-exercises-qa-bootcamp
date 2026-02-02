import random

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
    EC.visibility_of_element_located((By.CLASS_NAME, "places__list"))
)
# Save the title of the most recent card
title_before = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text
# Click the button to create a new card
driver.find_element(By.CLASS_NAME, "profile__add-button").click()
# Enter the name of the new place; it must be different from the most recent card
new_title = f"Tokio{random.randint(100, 999)}"
driver.find_element(By.NAME, "name").send_keys(new_title)
# Insert a link to the new photo
driver.find_element(By.NAME, "link").send_keys(
    "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")
# Save the data
driver.find_element(By.XPATH, ".//form[@name='new-card']/button[text()='Save']").click()
# Wait for the button that deletes the post to appear
WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
    (By.XPATH, "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']")))
# Verify that the card has the correct title
title_after = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']")
assert title_after.text == new_title
# Save the number of cards before deleting
cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
# Delete the card
driver.find_element(By.XPATH,
                    "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']").click()
WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(
    (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before))
# Verify that there is now one fewer card
cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_before - cards_after == 1

driver.quit()