

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("http://www.google.com/")
driver.maximize_window()


# search_element = driver.find_element(By.XPATH,"//textarea[@aria-owns='Alh6id']")
# search_element = driver.find_element(By.XPATH,"//textarea[@aria-controls='Alh6id']")
driver.find_element(By.CSS_SELECTOR,"input[name='APjFqb']").send_keys("Digi stacksoft")

# search_element.send_keys("Digi stacksoft")
search_element.click()
driver.maximize_window()
search_element.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()



