#X-path axes
#other types of X-path

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.get("https://money.rediff.com/gainers")

#self
text=driver.find_element(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/self::a").text
print(text)

#parent
parent=driver.find_element(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/parent::td").text
print(parent)

#child
childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Bhilwara Technical')]/ancestor::tr/child::td")
print(len(childs))

#ancestor
ancestor_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/ancestor::tr").text
print(ancestor_msg)

#descendant
descendant=driver.find_elements(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/ancestor::tr/descendant::*")
print(len(descendant))

#following
following=driver.find_elements(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/ancestor::tr/following::*")
print(len(following))

# #following-sibling
following_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Bhilwara Technical')]/ancestor::tr/following-sibling::tr")
print(len(following_sib))

#preceding
preceding=driver.find_elements(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/ancestor::tr/preceding::*")
print(len(preceding))

#preceding-sibling
preceding_sib=driver.find_elements(By.XPATH,"//a[normalize-space()='Bhilwara Technical']/ancestor::tr/preceding-sibling::*")
print(len(preceding_sib))

driver.close() 