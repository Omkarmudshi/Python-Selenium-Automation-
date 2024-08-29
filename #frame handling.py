#frame handling

#frame we use when web page had anothor webpage in it
#to access the frame 


import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH,"//*[@id='RESULT_TextField-0']").send_keys("omkar")
driver.switch_to.default_content()   #used to switch in to main page

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("mudshi")