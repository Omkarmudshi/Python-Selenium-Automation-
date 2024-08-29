#text action chain

#just like mouse we an control keyboad key through actionchain

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains     #action chain 
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")

driver=webdriver.Firefox(service=serv_obj)
driver.get("https://text-compare.com/")
driver.implicitly_wait(5)

input_1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")    #1st input box
input_2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")        #second
#to perform the we have to use actionchain for that we have to create fisrt the object of the action hain

input_1.send_keys("Omkar")
action=ActionChains(driver)
#input1 ctrl+a
time.sleep(2)
# action.key_down(Keys.CONTROL) #used to hold ctrl key button
# action.send_keys('a') # used to press a key to perform ctrl+a
# action.key_up(Keys.CONTROL) #used to release ctrl key
# action.perform()    #used to perform code

action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

time.sleep(2)
#copy input

action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#TAb

action.send_keys(Keys.TAB).perform() #used to navigate to sencond input box

#ctrl+v

action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
action.send_keys(Keys.SPACE).send_keys("mudshi").perform()
time.sleep(2)
driver.quit()