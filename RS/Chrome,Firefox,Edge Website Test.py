from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#------FIREFOX-----
service_obj = Service("/Users/DARSHAN BM/Downloads/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)

#Solarsquare
driver.get("https://www.solarsquare.in/")
driver.maximize_window()
time.sleep(5)
#Amzon
driver.get("https://www.amazon.in/gp/sva/dashboard")
driver.maximize_window()
time.sleep(5)

driver.close()











#
#
#
#
# driver.get("https://amazon.com")
# driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.forward()
#



















#------Chrome------
#service_obj= Service(":/Users/DARSHAN BM/Downloads/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)


#-------EDGE------
#ervice_obj = Service("C:/Users/DARSHAN BM/Downloads/msedgedriver.exe")
#driver = webdriver.Edge(service=service_obj)