from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
driver.maximize_window()
time.sleep(5)
food = driver.find_element(By.XPATH,"//select[@multiple='true']")

dropdown = Select(food)

dropdown.select_by_index(0)
# dropdown.select_by_index(1)
dropdown.select_by_index(2)

dropdown.select_by_visible_text('Bonda')

time.sleep(5)
dropdown.deselect_by_index(3)
time.sleep(5)


