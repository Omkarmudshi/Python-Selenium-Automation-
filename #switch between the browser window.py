#switch between the browser window
# 


import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

# windows=driver.window_handles
# print(windows)

driver.find_element(By.XPATH,"//button[normalize-space()='New Browser Window']").click()
windows=driver.window_handles
parent=windows[0]
child=windows[1]
print(parent,child)

driver.switch_to.window(parent)
print(driver.title)
time.sleep(2)
driver.switch_to.window(child)
print(driver.title)
driver.quit()