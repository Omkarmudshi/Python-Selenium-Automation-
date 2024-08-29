#handling mouse operation

#Action Chains
#1- mouse hover -- action.move_to_element(element_name).click().perform()
#2- right click -- action.context_click(element_name).perform()
#3- double click -- action.double_click(element_name).perform()
#4- drag and drop -- action.drag_and_drop(Sourse_name,Target_name).perform()
#

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains     #action chain 
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(5)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

rome_ele=driver.find_element(By.XPATH,"//div[@id='box6']")
italy_ele=driver.find_element(By.XPATH,"//div[@id='box106']")

washington_ele=driver.find_element(By.XPATH,"//div[@id='box3']")
us_ele=driver.find_element(By.XPATH,"//div[@id='box103']")

action=ActionChains(driver)

action.drag_and_drop(rome_ele,italy_ele).perform()
time.sleep(1)
action.drag_and_drop(washington_ele,us_ele).perform()
time.sleep(4)

driver.quit()