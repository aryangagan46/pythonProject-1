from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.maximize_window()
time.sleep(2)
#
# search_element = driver.find_element(By.ID,"APjFqb")
# time.sleep(2)
# """
# //tagname[@id='value']
# """
# search_element = driver.find_element(By.XPATH,"//textarea[@aria-controls='Alh6id']")
# search_element.send_keys("Gmail")
# search_element.send_keys(Keys.RETURN)
# time.sleep(3)
#
# search_element = driver.find_element(By.LINK_TEXT,"हिन्दी")
# search_element.send_keys(Keys.RETURN)
# time.sleep(3)
#
# # search_element = driver.find_element(By.PARTIAL_LINK_TEXT,"తెలు")
# # search_element.send_keys(Keys.RETURN)
#
# # search_element = driver.find_element(By.NAME,"q")
# # time.sleep(2)
#
# # search_element = driver.find_element(By.CLASS_NAME,"gLFyf")
# # search_element.send_keys("Gmail")
# # time.sleep(1)
# # search_element.send_keys(Keys.RETURN)
# # time.sleep(2)

search_element = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
search_element.send_keys("clinicia")
search_element.send_keys(Keys.RETURN)
time.sleep(2)
# #
"""
when there is no ID,CLASS,NAME,TAG you can make your own XPATH using ---->  //h3[normalize-space()='Login']
"""
#
search_element1 = driver.find_element(By.XPATH,"//h3[normalize-space()='Login']")
search_element1.click()
time.sleep(2)
#
search_element2 = driver.find_element(By.XPATH,"//*[@id='username']")
search_element2.send_keys("darshan10051992@gmail.com")
search_element2.send_keys(Keys.RETURN)
time.sleep(2)

search_element3 = driver.find_element(By.XPATH,"//*[@id='password']")
search_element3.send_keys("SterLIng*123W")
time.sleep(2)
#
search_element4 = driver.find_element(By.XPATH,"//button[@id='login']")
search_element4.click()
time.sleep(4)
ffgmhjxydudd
search_element5 = driver.find_element(By.XPATH,"//i[@title='Add New']")
search_element5.click()
time.sleep(2)
#
search_element6 = driver.find_element(By.XPATH,"//p[@class='sub_menu_txt']")
search_element6.click()
time.sleep(2)
#
search_element7 = driver.find_element(By.XPATH,"//input[@aria-required='true']")
search_element7.send_keys("Maddy")
search_element7.send_keys(Keys.RETURN)
time.sleep(2)
#
search_element8 = driver.find_element(By.XPATH,"//input[@id='p_mob']")
search_element8.send_keys("0000000000")
search_element8.send_keys(Keys.RETURN)
time.sleep(2)

search_element9 = driver.find_element(By.XPATH,"//button[@id='save_patient']")
search_element9.click()
time.sleep(2)
#
search_element10 = driver.find_element(By.XPATH,"//img[@alt='user-img']")
search_element10.click()
time.sleep(2)

search_element10 = driver.find_element(By.XPATH,"//a[normalize-space()='Logout']")
search_element10.click()
time.sleep(4)


# search_element10 = driver.find_element(By.PATH,"//button[@xpath='1']")
# search_element10.click()
# time.sleep(6)
# //i[@title='Add New']
# //i[@title='Setting']
# //span[normalize-space()='Patients']
# //i[@class='fa fa-whatsapp my-float']
# //a[normalize-space()='Logout'] ---------for  href



