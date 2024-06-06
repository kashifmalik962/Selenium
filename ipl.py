import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


chrome_opt = Options()
chrome_opt.add_argument('--headless')

driver = webdriver.Chrome()
driver.get('https://www.iplt20.com/stats/2024')

wait = WebDriverWait(driver,5)

# time.sleep(1.5)

view_all = '/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/div'
wait.until(EC.element_to_be_clickable((By.XPATH,view_all))).click()
time.sleep(4)

all_data = driver.find_elements(By.TAG_NAME,'tr')
print(all_data)
# for data in all_data:
#     print(data)
#     print(data.find_element(By.XPATH,'./td[1]').text)



# /html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[2]/td[1]
# /html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[2]/td[2]
# /html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[2]/td[14]