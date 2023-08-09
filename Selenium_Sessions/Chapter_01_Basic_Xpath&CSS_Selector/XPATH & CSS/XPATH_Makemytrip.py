from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

time.sleep(2)

login = driver.find_element(By.XPATH, "//input[@id='username']")
login.send_keys("dbmadiwalar@gmail.com")
print(driver.title)
time.sleep(2)