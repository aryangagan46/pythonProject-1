from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame("iframeResult")

driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("Hi Meowwww")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)


