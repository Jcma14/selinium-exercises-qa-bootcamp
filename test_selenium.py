# Import Selenium Webdriver
from selenium import webdriver

# Create a driver
driver = webdriver.Chrome()
driver.maximize_window() # Modo de pantalla completa

# Open a webpage
driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
assert '/signin' in driver.current_url

driver.quit()


