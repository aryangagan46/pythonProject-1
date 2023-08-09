from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(2)

#
Flipkart = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2doB4z']")
Flipkart.click()
time.sleep(4)



Flipkart1 = driver.find_element(By.XPATH,"//a[@class='_1_3w1N']")
Flipkart1.click()
time.sleep(4)

print(Flipkart1)
print(Flipkart1.get_attribute('name'))
print(Flipkart1.get_attribute('text'))
print(Flipkart1.get_attribute('class'))
print(Flipkart1.get_attribute('data-cy'))
print(Flipkart1.is_enabled())
time.sleep(5)






