from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

time.sleep(5)
driver.switch_to.frame(0)

action_chains = ActionChains(driver) #actiionchains instance creation

source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')

action_chains.drag_and_drop_by_offset(source,50,20).perform()
action_chains.drag_and_drop(source,target).perform()
time.sleep(5)
action_chains.drag_and_drop(source,target).perform()
time.sleep(5)
driver.close()