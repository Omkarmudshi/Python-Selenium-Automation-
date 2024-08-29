#handling web-table
#html table 

#there are two types of table 
#1 static web table
#2 dynamic web table

#******** This is a static table *********

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")

#1 conut no of rows and columns

tablerow=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))   #7
tablecolumn=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))   #4
print(tablerow,tablecolumn)

#2 read spacific row and column data 

tabledata=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]")
print(tabledata.text)

#3 read all the row and columns data

for r in range(2,tablerow+1):
    for c in range(1,tablecolumn+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text #this becomes a dynamic xpath
        #Xpath can not take the variables so for that we have to convert them into str and put them into above syntax
        #other wire it will show the error
        print(data,end="  ")
    print()
           
print("---------------------------------------------------------------------------------")


#4 conditional based retriving the data
# find the book name whose auther name is mukesh and get the value of the book them and print them

for r in range(2,tablerow+1):
    bookauthor=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if bookauthor=="Mukesh":
        print("Book Name = ",driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1] ").text)
        print("Price of Book = ",driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4] ").text)
     

driver.quit()