from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.maximize_window()
time.sleep(2)

"""******************************************************************************"""


"""XPATH - WITH ID"""
# search_element = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(3)

# """XPATH - WITH CLASS"""
# search_element = driver.find_element(By.XPATH,"//*[contains(@class,'gLFyf')]")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(2)

# """XPATH WITH ATTRIBUTE"""
# search_element = driver.find_element(By.XPATH,"//textarea[@maxlength='2048']")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(2)

"""******************************************************************************"""


# """CSS WITH ID"""
# search_element = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(2)
#
# """CSS - WITH CLASS"""
# search_element = driver.find_element(By.XPATH,"//*[contains(@class,'gLFyf')]")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(2)


#
# """CSS - WITH ATTRIBUTE"""
search_element = driver.find_element(By.CSS_SELECTOR,"*[autocapitalize]")
search_element.send_keys("Gmail")
search_element.send_keys(Keys.RETURN)
time.sleep(2)

















"""XPATH - BY CLASS_NAME"""
# search_element = driver.find_element(By.CLASS_NAME,"gLFyf")
# search_element.send_keys("Gmail")
# time.sleep(1)
# search_element.send_keys(Keys.RETURN)
# time.sleep(2)

"""XPATH - By CSS_SELECTOR"""
# search_element = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(2)
#

"""
//tagname[@id='value']
"""

#
# search_element = driver.find_element(By.LINK_TEXT,"हिन्दी")
# search_element.send_keys(Keys.RETURN)
# time.sleep(3)
#
# search_element = driver.find_element(By.PARTIAL_LINK_TEXT,"తెలు")
# search_element.send_keys(Keys.RETURN)
#
# search_element = driver.find_element(By.NAME,"q")
# time.sleep(2)
#

