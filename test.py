import ast
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()
# Now you can use the driver for testing with the extension pre-loaded in headless mode
txt = open("trackPath.txt")

step=ast.literal_eval('[' + txt.read() + ']')
txt.close()
driver.get("http://127.0.0.1:5000")
page_source = driver.page_source
actions = ActionChains(driver)
wait = WebDriverWait(driver, 5)
for i in step:
    # print(i)
    wait.until(EC.element_to_be_clickable((By.XPATH, i[0]))).click()
    if len(i[1]) >=1 :
        for j in i[1]:
            # print(j)
            inputValue =  j[0]
            string = j[1]
            wait.until(EC.element_to_be_clickable((By.XPATH,inputValue))).click()
            actions.send_keys(string)
            actions.perform()
            # input()
    if i[2] != []:
        driver.get(i[2])
        
print("script Execute Successfully")