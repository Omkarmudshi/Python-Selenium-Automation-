#locators


import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
sev_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=sev_obj)
driver.get("https://amazon.in/")
#time.sleep(60)
#driver.maximize_window()
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("laptops")
sliders=driver.find_elements(By.CLASS_NAME,"a-carousel-card")
print(f"sliders: {len(sliders)}")
link=driver.find_elements(By.TAG_NAME,"a")
print(f"<a> link: {len(link)}")