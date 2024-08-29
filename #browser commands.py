#browser commands
#selenium webdriver catagory commands

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")

#close()

driver.close() #used to kill single process or browser window
               #only parent window is close. the first page get kill

driver.quit() #used to kill multiple process or browser window
               #it kill driver process internaly 