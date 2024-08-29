#alert handling

#for accesing the alert window we have to use driver.switch_to.alert method
# to capture the alert box we have to create variable/object for it
# to select Yes/No option we have to use accpte for yes and dismiss method for reject/cansel
# to send some data i it we have to use send_keys method  

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#this will open the alert window
# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(1)

# alertwindow=driver.switch_to.alert
# print(alertwindow.text)
# alertwindow.send_keys("omkar")
# #alertwindow.accept()       #to click on yes
# alertwindow.dismiss()       #to click on cancel

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
driver.switch_to.alert.accept()
time.sleep(2)
driver.quit()
