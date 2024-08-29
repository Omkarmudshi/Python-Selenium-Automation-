#calendar picker
# two types of elements there

# standard elements- means they remains same thoughout the page  eg button,radio button
# Non-standard elements means there are changeble or costomizeble  eg date picker 

#the similar script does not work for all date picker
#the devloper creATE date pick picker based on there requidment so they are diff in every webpage based on requiedment

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)

#1 type 1

driver.get("https://jqueryui.com/datepicker/")
print("ok")
driver.switch_to.frame(0) #switch to frame
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("07/29/2000")

#type 2

month="July"
year="2025"
day="29"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yea=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon==month and yea==year:
        break
    else :
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #next

date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for d in date:
    if d.text==day:
        d.click()
        break

time.sleep(2)
driver.quit()