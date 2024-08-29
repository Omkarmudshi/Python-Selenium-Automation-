#conditional commands
#selenium webdriver catagory commands

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")
#is_displayed()  is_enabled
searchbox=driver.find_element(By.XPATH,"//input[@id='first_name']")
print("displayed :",searchbox.is_displayed())
print("Enabled :",searchbox.is_enabled())

#is_selected  //only use for radio button are selected or not

male=driver.find_element(By.XPATH,"//input[@id='radio_1665627729_Male']")
female=driver.find_element(By.XPATH,"//input[@id='radio_1665627729_Female']")

male.click()
female.click()
# time.sleep(5)
print("Male",male.is_selected())
print("female",female.is_selected())

driver.close()