from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://ksrtc.in/oprs-web/")
driver.maximize_window()
time.sleep(2)


KSRTC = driver.find_element(By.XPATH,"//input[@size='22']")
KSRTC.send_keys("HUBBALLI")
KSRTC.click()
time.sleep(2)

KSRTC0 = driver.find_element(By.XPATH,"//a[@id='ui-id-3']")
KSRTC0.click()
time.sleep(2)

KSRTC1 = driver.find_element(By.XPATH,"//input[@id='toPlaceName']")
KSRTC1.send_keys("PUNE")
KSRTC1.click()
time.sleep(6)

KSRTC3 = driver.find_element(By.XPATH,"//a[@id='ui-id-3']")
KSRTC3.click()
time.sleep(6)