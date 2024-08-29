#DropDown handling

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# for select we have to use select 
#for drop down
from selenium.webdriver.support.select import Select

serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

drop_country=Select(driver.find_element(By.XPATH,"//select[@id='country']"))

drop_country.select_by_visible_text("China")   #by element text  mostly use this method
time.sleep(1)
drop_country.select_by_value("india")       #by value attribute from webelement
time.sleep(1)
drop_country.select_by_index(0)  # select by index no
time.sleep(1)

#capture all the optioins from dropdown
alloptions=drop_country.options
print(len(alloptions))

#printing the all options from dropdown

for op in alloptions:
    print(op.text)
 
driver.quit()