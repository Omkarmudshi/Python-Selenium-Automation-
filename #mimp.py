#mimp

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://amazon.in")

#find_element() -it return single webelement
# element1=driver.find_element(By.XPATH,"//div[@class='navLeftFooter nav-sprite-v1']//a")
# element1.send_keys("sandals")

# #locator maching with multiple webelements

# element=driver.find_element(By.XPATH,"//div[@class='navLeftFooter nav-sprite-v1']//a")
# print(element.text)

# if element is not present then it gives error
# #no such element exception-when element is not found then this error occures
# ligin=driver.find_element(By.XPATH,"")


#----------------------------------------------------------------------------

#find_elements
#-acessing single element using find_elements method
elements=driver.find_elements(By.XPATH,"//div[@class='navLeftFooter nav-sprite-v1']//a")
print(len(elements))
#here find_elements return the webelements in list format
#if we want to access the elements then we need to use or 
#send some keys into it for that we have to use index number 
# other wise it give an error
elements[0].send_keys("sandals for men")

# mutiple elements
elements1=driver.find_elements(By.XPATH,"//div[@class='navLeftFooter nav-sprite-v1']//a")
print(len(elements1))
for ele in elements1:
    print(ele.text)


#if element is not available then it does not give any 
# error unlike fid_element

driver.quit()