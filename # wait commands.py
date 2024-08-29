# wait commands
#implicitly_wait
# used to solve synchronization problem

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

sev_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=sev_obj)
driver.implicitly_wait(5)   #i put this command before get method becouse if we ocure syncronization
                            #problem in any line of code it will handle easily 
                            #it will apply to every line of code or command
driver.get("https://google.com/")
searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()
driver.find_element(By.XPATH,"//a[@href='https://www.selenium.dev/']").click()
driver.quit()
