from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
time.sleep(6)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("1234")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(7)
driver.switch_to.alert.accept()
time.sleep(6)
