from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()

driver.get("https://www.makemytrip.com/")
driver.maximize_window()

time.sleep(5)
driver.implicitly_wait(10)

explicit_wait = WebDriverWait(driver,10)
explicit_wait.until(ec.element_to_be_clickable((By.LINK_TEXT,"Flights"))).click()

# login = driver.find_element(By.LINK_TEXT,"Flights").click()   #replaced with above 2 lines
#
# time.sleep(5)

login = driver.find_element(By.XPATH,"//a[normalize-space()='Domestic Flights']").click()

explict_wait = WebDriverWait(driver,10)
explict_wait.until(ec.element_to_be_clickable((By.XPATH,"//input[@id='fromCity']"))).click()

time.sleep(10)