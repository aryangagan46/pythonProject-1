from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.abhibus.com/")
driver.maximize_window()
time.sleep(2)

LOGIN = driver.find_element(By.XPATH, "//span[@id='AccLogin']")
LOGIN.click()
time.sleep(2)

LOGIN2 = driver.find_element(By.XPATH,"//input[@id='mobileNo']")
LOGIN2.send_keys("7829174373")
time.sleep(3)

LOGIN3 = driver.find_element(By.XPATH,"//input[@tabindex='7']")
LOGIN3.click()
time.sleep(3)

print("OTP Was sent to Registered Number Successfully")