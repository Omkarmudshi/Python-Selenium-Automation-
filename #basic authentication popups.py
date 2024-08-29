#basic authentication popups
#the authentication popups are not the html element those are diff application elements
#  we use inject direct username and password directly on url to bypass the authentication
 


import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
# Normal url- https://the-internet.herokuapp.com/basic_auth
# Bypass url -https://admin:admin@the-internet.herokuapp.com/basic_auth
# syntax https://username:password@domainname.com
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)