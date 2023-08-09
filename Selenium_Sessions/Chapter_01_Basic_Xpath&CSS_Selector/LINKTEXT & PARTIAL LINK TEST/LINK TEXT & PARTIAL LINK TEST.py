from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(10)

login = driver.find_element(By.LINK_TEXT,"Yatra for Business")
login.send_keys(Keys.RETURN)
time.sleep(15)

