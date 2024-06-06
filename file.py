import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome()
wait = WebDriverWait(driver,4)
driver.get('https://www.adamchoi.co.uk/overs/detailed')


path = '/html/body/div[2]/div/div/div[2]/div/home-away-selector/div/div/div/div/label[2]'
wait.until(EC.element_to_be_clickable((By.XPATH,path))).click()

dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')
time.sleep(3)

date = []
home_team = []
score = []
away_team = []


all_mathes = driver.find_elements(By.TAG_NAME, 'tr')
for row in all_mathes:
    date.append(row.find_element(By.XPATH,'./td[1]').text)
    home_team.append(row.find_element(By.XPATH,'./td[2]').text)
    score.append(row.find_element(By.XPATH,'./td[3]').text)
    away_team.append(row.find_element(By.XPATH,'./td[4]').text)


df = pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_tem':away_team})
print(df)
df.to_csv('goal.csv',index=False)