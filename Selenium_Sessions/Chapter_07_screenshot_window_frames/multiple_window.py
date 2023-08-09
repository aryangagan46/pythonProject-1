from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(10)

S = driver.find_element(By.XPATH,"//div[contains(@class,'flexOne')]")
if "Super Offers" in S.text:
    S.click()

print(driver.current_url)

main_window = driver.current_window_handle

print(main_window)
time.sleep(5)
windows_list = driver.window_handles
print(windows_list)

for window in windows_list:
    print("ITERATION")
    if window != main_window:
        print("we are in sub window")
        driver.switch_to.window(window)
        print(driver.current_window_handle)
        driver.find_element(By.XPATH,"//label[@for='FLT']").click()
        time.sleep(5)
        driver.close()
        time.sleep(3)

driver.switch_to.window(main_window)