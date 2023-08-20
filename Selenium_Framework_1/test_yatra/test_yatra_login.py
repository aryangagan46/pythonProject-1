from Selenium_Framework_1.selenium_config import Yatra
from Selenium_Framework_1.selenium_xpath import YatraXpath
from Selenium_Framework_1.selenium_utilities import *

import time
class YatraLogin():
    def login(self):

        utility = SeleniumUtilities()

        driver = utility.launch_browser(Yatra.yatra_url)

        login_title = utility.get_title(driver, YatraXpath.login)

        print("TITLE", login_title)

        utility.send_keys(driver, YatraXpath.login, "test1@gmail.com", 'css')

yatra_obj = YatraLogin()
yatra_obj.login()