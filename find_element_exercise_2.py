from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(5)
# Find all elements
elements = driver.find_elements(By.XPATH, ".//img")
# Debug: print how many elements were found
print(f"Number of elements <img> found: {len(elements)}")
# Debug: print the elements found
for i, element in enumerate(elements):
    print(f"Element {i+1}: {element.get_attribute('src')}")

assert len(elements) > 1, f"Expected more than 1 <img> element, but found {len(elements)}"
# Check that the number of elements found is greater than 1 using len()
assert len(elements) > 1, f"Expected more than 1 element, but found {len(elements)}"
# Close browser
driver.quit()