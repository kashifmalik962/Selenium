import pandas as pd
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

# Count
count = 1

# Columns of data
columns = []
column_name = 1

# Each columns data
pos = []
player = []
mat = []
inns = []
no = []
runs = []
hs = []
avg = []
bf = []
sr = []
C100 = []
F50 = []
S4 = []
S6 = []


all_data = driver.find_elements(By.TAG_NAME,'tr')
for data in all_data:
    # print(data.text)
    if data.find_elements(By.TAG_NAME,'td'):
        pos.append(data.find_element(By.XPATH,'./td[1]').text)
        player.append(data.find_element(By.XPATH,'./td[2]').text)
        print(player)
        mat.append(data.find_element(By.XPATH,'./td[3]').text)
        inns.append(data.find_element(By.XPATH,'./td[4]').text)
        no.append(data.find_element(By.XPATH,'./td[5]').text)
        runs.append(data.find_element(By.XPATH,'./td[6]').text)
        hs.append(data.find_element(By.XPATH,'./td[7]').text)
        avg.append(data.find_element(By.XPATH,'./td[8]').text)
        bf.append(data.find_element(By.XPATH,'./td[9]').text)
        sr.append(data.find_element(By.XPATH,'./td[10]').text)
        C100.append(data.find_element(By.XPATH,'./td[11]').text)
        F50.append(data.find_element(By.XPATH,'./td[12]').text)
        S4.append(data.find_element(By.XPATH,'./td[13]').text)
        S6.append(data.find_element(By.XPATH,'./td[14]').text)
    
    else:
        if count == 1:
            columns.append(data.find_element(By.XPATH,'./th[1]').text)
            columns.append(data.find_element(By.XPATH,'./th[2]').text)
            columns.append(data.find_element(By.XPATH,'./th[3]').text)
            columns.append(data.find_element(By.XPATH,'./th[4]').text)
            columns.append(data.find_element(By.XPATH,'./th[5]').text)
            columns.append(data.find_element(By.XPATH,'./th[6]').text)
            columns.append(data.find_element(By.XPATH,'./th[7]').text)
            columns.append(data.find_element(By.XPATH,'./th[8]').text)
            columns.append(data.find_element(By.XPATH,'./th[9]').text)
            columns.append(data.find_element(By.XPATH,'./th[10]').text)
            print(columns)
            columns.append(data.find_element(By.XPATH,'./th[11]').text)
            columns.append(data.find_element(By.XPATH,'./th[12]').text)
            columns.append(data.find_element(By.XPATH,'./th[13]').text)
            columns.append(data.find_element(By.XPATH,'./th[14]').text)
            count+=1
        else:
            break

df = pd.DataFrame({columns[0]:pos, columns[1]:player, columns[2]:mat, columns[3]:inns, columns[4]:no,
              columns[5]:runs, columns[6]:hs, columns[7]:avg, columns[8]:bf, columns[9]:sr,
              columns[10]:C100, columns[11]:F50, columns[12]:S4, columns[13]:S6})

df.to_csv('IPL.csv',index=False)


# /html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[1]
# /html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[1]/th[12]
# /html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[1]/th[1]