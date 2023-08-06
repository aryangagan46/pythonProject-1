from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)

login = driver.find_element(By.LINK_TEXT, "Flights").click()
time.sleep(5)

login1 = driver.find_element(By.XPATH, "//a[text()='Domestic Flights']").click()
time.sleep(4)

fp = driver.find_element(By.XPATH, "//label[@for='fromCity']").click()
time.sleep(5)

dropdown = driver.find_element(By.XPATH, "//p[text()='Mumbai, India']").click()
time.sleep(5)


cities = ['Mumbai, India', 'Bangkok, Thailand','Bengaluru, India']

for i in cities:

    fp = driver.find_element(By.XPATH, "//input[@id ='fromCity']").click()
    time.sleep(3)
    ele = "//p[text()='ARGUMENT']"

    #ele = '//p[text()=' +i +']'
    #print("concatination",ele)

    ele1 = ele.replace('ARGUMENT', str(i))
    print(ele1)
    city = driver.find_element(By.XPATH,ele1)
    city.click()
    time.sleep(5)
