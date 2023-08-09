from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

time.sleep(5)

doctors_option = driver.find_element(By.XPATH,"//p[contains(text(),'Doctors & Nurses ')]//br")
act_chains = ActionChains(driver)

act_chains.move_to_element(doctors_option).perform()

time.sleep(5)
driver.find_element(By.XPATH,"//p[contains(text(),'Doctors & Nurses ')]").click()

time.sleep(5)