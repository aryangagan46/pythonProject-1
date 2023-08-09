from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")
driver.maximize_window()
time.sleep(2)


Google_Search = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
Google_Search.send_keys("Flipkart")
Google_Search.send_keys(Keys.RETURN)
time.sleep(5)


Flipkart = driver.find_element(By.CSS_SELECTOR,"h3.LC20lb.MBeuO.DKV0Md")
Flipkart.click()
time.sleep(6)

Flipkart1 = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
Flipkart1.send_keys(Keys.ESCAPE)
time.sleep(6)

Flipkart2 = driver.find_element(By.XPATH,"//input[@name='q']")
Flipkart2.send_keys("OnePlus Nord 2t")
Flipkart2.send_keys(Keys.RETURN)
time.sleep(6)
#
Flipkart3 = driver.find_element(By.XPATH,"//div[@id='container']//div[@class='_3PzNI-']")
Flipkart3.click()
# print(Flipkart3)
time.sleep(6)

Flipkart4= driver.find_element(By.XPATH,"//div[@id='container']//div[@class='_3PzNI-']").is_selected()
print("Checkbox is ",Flipkart4)
time.sleep(3)