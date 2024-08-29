from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe')
#from webdriver_manager.chrome import ChromeDriverManager
cService = webdriver.ChromeService(executable_path='C:\Test_Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Firefox(service = serv_obj)
#driver=webdriver.Chrome("")
driver.get("https://youtube.com")
driver.find_element(By.NAME,"search_query").send_keys("infinity war")
driver.find_element(By.ID,"search-icon-legacy").click()
#driver.find_element(By.CLASS_NAME,"Passw").send_keys("admin")
#driver.find_element(By.CLASS_NAME,"button-1 login-button").click()
























