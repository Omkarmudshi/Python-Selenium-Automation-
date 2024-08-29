#checkbox handling
#https://testautomationpractice.blogspot.com/

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

checkboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id,'day')]")
# #selecting all checkboxes
# for checkbox in checkboxes:
#     checkbox.click()

# #selecting all checkboxes by using range 

# for i in range (len(checkboxes)):
#     checkboxes[i].click()

# #selecting only monday and sunday
# for i in checkboxes:
#     day=i.get_attribute('id')
#     if day=="monday" or day=="sunday":
#         i.click()
# time.sleep(5)
# driver.quit()

# #selectinfg last 2 days

for checkbox in range (len(checkboxes)-2,len(checkboxes)):
    checkboxes[checkbox].click()


time.sleep(5)
## unselecting the checkboxes

for chechbox in checkboxes:
    if chechbox.is_selected():
        chechbox.click()    #for unselecting the selected checkbox

driver.quit()