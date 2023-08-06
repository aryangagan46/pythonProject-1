from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)

driver1 = driver.find_element(By.TAG_NAME,"p").click()
time.sleep(4)

