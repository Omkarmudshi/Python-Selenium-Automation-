#Navigational commands commands
#selenium webdriver catagory commands

#back()
#forward()
#refresh()

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://demo.wpeverest.com/user-registration/guest-registration-form/")

driver.get("https://amazon.in")
time.sleep(2)
driver.back()   #going back to previous page registerpage
time.sleep(2)
driver.forward() #going back to next page registerpage
driver.refresh()    #refresh the current page 
driver.quit()   #kill all the process

