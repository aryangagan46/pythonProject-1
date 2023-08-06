from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(10)

login = driver.find_element(By.LINK_TEXT,"Flights").click()
time.sleep(5)

login = driver.find_element(By.XPATH,"//a[text()='Domestic Flights']").click()

time.sleep(5)
#
fp = driver.find_element(By.XPATH,"//label[@for='fromCity']").click()
time.sleep(5)

dropdown = driver.find_element(By.XPATH,"//p[text()='Mumbai, India']").click()
time.sleep(5)

fp1 = driver.find_element(By.XPATH,"//label[@for='toCity']").click()
time.sleep(5)

dropdown1 = driver.find_element(By.XPATH,"//p[text()='Bengaluru, India']").click()
time.sleep(15)

search = driver.find_element(By.XPATH,"//a[text()='Search']").click()
time.sleep(20)