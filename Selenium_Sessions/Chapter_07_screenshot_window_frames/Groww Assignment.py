from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://groww.in/blog/category/stocks")
driver.maximize_window()
time.sleep(5)
driver.implicitly_wait(30)

dri

all_bodys = driver.find_elements(By.TAG_NAME,'body')
print(len(all_bodys))


all_script = driver.find_elements(By.TAG_NAME,'link')
print(type(all_script))
print(len(all_script))


images_list = driver.find_elements(By.XPATH,"//div[@class = 'pos-rel']")
print(len(images_list))
print(len(images_list))


right_click_option = driver.find_element(By.XPATH,"//input[@id='globalSearch23']")
act_chains = ActionChains(driver)


act_chains.context_click(right_click_option).perform()
