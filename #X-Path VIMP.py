#X-Path VIMP
#Partial X-Path/relative X-path = //*[@id="u_0_5_mx"]
#Full x-path/Absolute X-PAth = /html/body/div[1]/div[1]/div[1]/div/div/di v/div[2]/div/div[1]/form/div[2]/button

#selectorshub locator eg of youtube search abs xpath
#/html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[4]/div[2]/ytd-searchbox[1]/form[1]/div[1]/div[1]/input[1]


import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

sev_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=sev_obj)
driver.get("https://www.amazon.in/")
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys("sandals") #absolute X-Path
# driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click() #relative X-Path
# driver.find_element(By.XPATH,"")
#//span[contains(text(),"Men's Lightweight Classic Clogs || Sandals with Ad")]

#contains() and startwith()
# driver.find_element(By.XPATH,"//input[contains(@id,'twotabsearchtextbox')]").send_keys("sandals")
driver.find_element(By.XPATH,"//a[text()='Amazon miniTV']").click()