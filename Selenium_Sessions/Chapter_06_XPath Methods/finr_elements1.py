from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://groww.in/blog/category/stocks")

driver.maximize_window()
time.sleep(5)

all_divs = driver.find_elements(By.TAG_NAME,'div')
print(len(all_divs))


all_inputs = driver.find_elements(By.TAG_NAME,'input')
print(type(all_inputs))
print(len(all_inputs)) #placeholder

login =  driver.find_elements(By.XPATH,"//span[contains(text(),'Login/Register')]")

print(login[0].get_attribute("text")) #why None??
print(login[0].text)

images_list = driver.find_elements(By.XPATH,"//div[@class = 'pos-rel']")
print(len(images_list))

images_list_starts_with = images_list = driver.find_elements(By.XPATH,"//div[starts-with(@class,'bc781')]")
print(len(images_list_starts_with))

contains_example = driver.find_elements(By.XPATH,"//div[starts-with(@class,'bc781')]//div//img[contains[@class,'Image')]")
print(len(contains_example))