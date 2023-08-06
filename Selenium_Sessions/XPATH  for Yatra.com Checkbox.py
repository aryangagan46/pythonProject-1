from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(5)

# confirmation = driver.find_element(By.XPATH,"//a[@title='Non Stop Flights']").is_selected()
# print("CONFIRMATION STATUS",confirmation)
# time.sleep(4)

# try:
#     flights_checkbox = driver.find_element(By.XPATH,"//a[@title='Non Stop Flights']//i[@class='ico ico-checkbox ico-checkbox-checked']").is_displayed()
#     checkbox = True
#
# except:
#     print("exception")
#     checkbox = False
#     flights_checkbox = driver.find_element(By.XPATH,"//a[@title='Non Stop Flights']//i[@class='ico ico-checkbox']").is_displayed()
# time.sleep(5)
#
# if not checkbox:
#     print("checkbox not enabled hence clicking on it")
#     driver.find_element(By.XPATH,"//a[@title='Non Stop Flights']//i[@class='ico ico-checkbox']").click()
#     time.sleep(5)
# else:
#     print("it looks like flights options already enabled hence no need to click on it")

#*******************************************************************************************

# confirmation = driver.find_element(By.XPATH,"//li[@id='special_student_offer']").is_selected()
# print("CONFIRMATION STATUS",confirmation)
# time.sleep(4)
#
# try:
#     flights_checkbox = driver.find_element(By.XPATH,"//li[@id='special_student_offer']//i[@class='ico ico-checkbox ico-checkbox-checked']").is_displayed()
#     checkbox = True
#
# except:
#     print("exception")
#     checkbox = False
#     flights_checkbox = driver.find_element(By.XPATH,"//li[@id='special_student_offer']//i[@class='ico ico-checkbox']").is_displayed()
# time.sleep(5)
#
# if not checkbox:
#     print("checkbox not enabled hence clicking on it")
#     driver.find_element(By.XPATH,"//li[@id='special_student_offer']//i[@class='ico ico-checkbox']").click()
#     time.sleep(5)
# else:
#     print("it looks like flights options already enabled hence no need to click on it")
#
#*******************************************************************************************
