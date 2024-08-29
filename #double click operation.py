#handling mouse operation

#Action Chains
#1- mouse hover -- action.move_to_element(element_name).click().perform()
#2- right click -- action.context_click(element_name).perform()
#3- double click -- action.double_click(element_name).perform()
#4- drag and drop
#

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains     #action chain 
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")

driver=webdriver.Firefox(service=serv_obj)
driver.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_dblclick")
driver.implicitly_wait(5)

driver.switch_to.frame("iframeResult")  #switch to frame
dbclick=driver.find_element(By.XPATH,"//p[normalize-space()='Double-click on this paragraph.']")
action=ActionChains(driver)

action.double_click(dbclick).perform()  #perform double click action
