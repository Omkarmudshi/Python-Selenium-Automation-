#Explicit_wait
# used to solve synchronization problem

import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sev_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=sev_obj)
explicit=WebDriverWait(driver,2, ignored_exceptions=[NoSuchElementException, TimeoutException])    
#here we created object for explicit_wait with the WebDriverWait method along with driver object,time(10),and exception handler
#here in explicit_wait we can handle exceptio very easily with one line of code unlike implicit_wait where we have to use try catch block to handle exception
#that why it is very best way to use insted of implicit_wait command
# for this we have to import webdriverwait library
# and expected conditons too 
driver.get("https://google.com/")
searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium000")
searchbox.submit()
seleniumsearch=explicit.until(EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.selenium.dev/']")))
#here insted of find_element we use until method with EC(expected_conditons)and presence_of_element_located
#becouse we are going to find the element from webpage ultil that element get present on the page after locating that element the specific opration will perform accordingly
#if it does not find that element with in 10 sec as we mention in explicit object and then it handle the error (eception) and perform next opration as we assign in script
seleniumsearch.click()
driver.quit()