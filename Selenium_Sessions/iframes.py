from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get("https://chercher.tech/practice/frames")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='frame1']"))
topic = driver.find_element(By.XPATH,"//body//input")
topic.click()
topic.send_keys("hello")

time.sleep(8)



