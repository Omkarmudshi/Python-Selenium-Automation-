#application commands
#selenium webdriver catagory commands

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://amazon.in/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()