#broken link handling

import requests as requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
links=driver.find_elements(By.XPATH,"//a")
count=0
for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"  Broken Link")
        count+=1
    else:
        print(url,"  Valid Link")
print(count)
driver.quit()