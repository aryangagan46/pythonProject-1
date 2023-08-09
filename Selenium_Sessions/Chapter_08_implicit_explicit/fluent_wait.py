from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException

import time

driver = webdriver.Chrome()

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(5)
explicit_wait = WebDriverWait(driver,10,2,ignored_exceptions=[ElementClickInterceptedException])
explicit_wait.until(ec.element_to_be_clickable((By.LINK_TEXT,"Flights"))).click()

time.sleep(10)
login = driver.find_element(By.XPATH,"//a[normalize-space()='Domestic Flights']").click()

time.sleep(5)