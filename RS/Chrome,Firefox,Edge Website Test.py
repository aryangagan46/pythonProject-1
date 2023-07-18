from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#------Chrome------
#service_obj= Service(":/Users/DARSHAN BM/Downloads/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

#------FIREFOX-----
service_obj = Service("/Users/DARSHAN BM/Downloads/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)

#-------EDGE------
#ervice_obj = Service("C:/Users/DARSHAN BM/Downloads/msedgedriver.exe")
#driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://www.solarsquare.in/")
print(driver.title)
print(driver.current_url)
driver.get("https://amazon.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
