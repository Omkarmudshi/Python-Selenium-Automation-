#slider bar operation

#for conrtoling the horizontal slide bar we use drag_and_drop_offset
#syntax  -- action.drag_and_drop_offset(min/max,x axis,y axis)
#          0if we want to drag from backward just put -x axis for that

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains     #action chain 
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(2)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider=driver.find_element(By.XPATH,"//span[1]")
max_slider=driver.find_element(By.XPATH,"//span[2]")

print("location of slider Before Moving")

print(min_slider.location)  #{'x': 59, 'y': 250}
print(max_slider.location)  #{'x': 517, 'y': 250}

action=ActionChains(driver)

action.drag_and_drop_by_offset(min_slider,100,0).perform() 

action.drag_and_drop_by_offset(max_slider,-100,0).perform()

print("location of slider after Moving")
print(min_slider.location)  # {'x': 160, 'y': 250}
print(max_slider.location)  # {'x': 416, 'y': 250}
time.sleep(2)
driver.quit()