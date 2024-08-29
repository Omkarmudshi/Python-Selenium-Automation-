#Css selectors VIPM
#in css selector tag name are optional we can simply use there id name and class name for that we haqve to use syntax
#for id we have to use "#" sign in front of id value e.g #idname or input#idname
#for class we have to use "." sign in front of class value eg .classname or input.classname
#if we dont have id and class name or we cas say we cant use id and class name that time wer can use tag attribute
# to select the elements. eg if we have page with multiple elements with same tag name and same id name and class name
# that time tag attibute get used for electin gthe elements  
#
# tag id - tagname#valueofid eg input#username
# tag class - tagname.valueofclass eg input.Username
# tag attribute - tagname.[attribute=value] eg input[data-testid=royal_email]
# tag class attribute - tagname.valueofclass[attribute=value]
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

sev_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=sev_obj)
driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"._9npi").send_keys("1234")
driver.find_element(By.CSS_SELECTOR,"button[data-testid=royal_login_button]").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
time.sleep(1)
driver.quit()