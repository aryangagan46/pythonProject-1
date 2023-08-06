from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

time.sleep(10)
login = driver.find_element(By.CSS_SELECTOR,"p[data-cy='LoginHeaderText']").click()


email = driver.find_element(By.XPATH,"//input[@id='username']")
email.click()

email.screenshot(".\\test.png")

driver.get_screenshot_as_file(r"C:\Users\DARSHAN BM\Documents\python screenshot\Darshan.png")