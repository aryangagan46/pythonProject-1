from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#options = webdriver.ChromeOptions() #----#For Chrome should open use this condition-----------
#options.add_experimental_option("detach", True) #-------#For Chrome should open use this  condition-----------

service_obj = Service("C:/Users/DARSHAN BM/Downloads/geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)

#driver = webdriver.Chrome(options=options) #-----#For Chrome should open use this condition-----------
driver.get("https://rahulshettyacademy.com/angularpractice/") 


driver.find_element(By.NAME, "email").send_keys("xyz@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")

#Creating Xpath for any element

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

#Creating Xpath for any element
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Darshan")
assert "Success" in message


#driver.find_element(By.XPATH, "//input[@name='identifier']").send_keys("asdhasdkabc")