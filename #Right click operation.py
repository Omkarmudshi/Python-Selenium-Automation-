#handling mouse operation

#Action Chains
#1- mouse hover -- action.move_to_element(element_name).click().perform()
#2- right click -- action.context_click(element_name).perform()
#3- double click
#4- drag and drop
#

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains     #action chain 
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")

driver=webdriver.Firefox(service=serv_obj)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.implicitly_wait(5)

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

action=ActionChains(driver)

action.context_click(button).perform()    #used to perform right action
#perform is must
time.sleep(5)
driver.close()