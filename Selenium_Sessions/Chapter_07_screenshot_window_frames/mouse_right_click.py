from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_oncontextmenu_html")
driver.maximize_window()

right_click_option = driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")

act_chains = ActionChains(driver)

act_chains.context_click(right_click_option).perform()
time.sleep(5)