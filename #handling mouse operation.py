#handling mouse operation

#Action Chains
#1- mouse hover -- .move_to_element(element_name).click.perform
#2- right click
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
driver.get("https://www.pepperfry.com/?gad_source=1&gclid=EAIaIQobChMI59zlurSSiAMV_hKDAx28kzkFEAAYASAAEgKHavD_BwE")

furniture=driver.find_element(By.XPATH,"//a[normalize-space()='Furniture']")
sofas=driver.find_element(By.XPATH,"//a[normalize-space()='Sofas & Seating']")
homedecor=driver.find_element(By.XPATH,"//a[normalize-space()='Home Decor']")
#to perform the mouse hover action
#we have to import ActionChain package from selenium webdriver
#we need to create action chain class object

action=ActionChains(driver) #created the action chain object
#when we create action object then we must have to pass the driver instence in it
#otherwise it will give us an error

#mouse hover action
#we have to use perform method to perform the action without it we can not perform any action
#perform method is must
time.sleep(2)
action.move_to_element(furniture).move_to_element(sofas).move_to_element(homedecor).click().perform()

time.sleep(2)
click=driver.find_element(By.XPATH,"//a[normalize-space()='Table Vases']")

click.click()
time.sleep(2)
driver.close()
