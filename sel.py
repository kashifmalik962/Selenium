from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
# Navigate to the Selenium Easy website
driver.get('https://www.google.com/')
print(driver.title)
time.sleep(1)

driver.get('https://translate.google.co.in/?sl=en&tl=hi&op=translate')
print(driver.title)
time.sleep(1)

driver.back()
driver.get('https://www.google.com/')
print(driver.title)
time.sleep(1)


driver.forward()
driver.get('https://translate.google.co.in/?sl=en&tl=hi&op=translate')
print(driver.title)
time.sleep(1)

# driver.maximize_window()
# driver.minimize_window()