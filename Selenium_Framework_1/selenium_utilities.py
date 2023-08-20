
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class SeleniumUtilities():

    def __init__(self):
        pass

    def get_title(self,driver,element):

        """
        get the title of element
        :param driver:
        :param element:
        :return:
        """

        element = element

        print("getting the title of element", element)
        title_field = driver.find_element(By.CSS_SELECTOR,element).get_attribute('title')
        return title_field

    def chrome_driver(self):
        global DRIVER
        options = Options()
        options.add_argument("--start-maximized")
        DRIVER = webdriver.Chrome(r"options=options")
        return DRIVER

    def launch_browser(self,url):
        DRIVER = self.chrome_driver()
        DRIVER.get(url)
        return DRIVER

    def send_keys(self,driver,element,text,category):
        if category == 'css':
            driver.find_element(By.CSS_SELECTOR,element).send_keys(text)
        if category == 'xpath':
            driver.find_element(By.XPATH,element).send_keys(text)
