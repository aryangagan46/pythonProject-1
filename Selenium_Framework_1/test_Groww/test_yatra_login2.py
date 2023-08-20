from Selenium_Framework_1.selenium_config import Yatra
from Selenium_Framework_1.selenium_xpath import YatraXpath
from Selenium_Framework_1.selenium_utilities import *
import unittest
import time

class YatraLogin(unittest.TestCase):

    def setUp(self):
        print("start the test suite")
        super(YatraLogin,self).setUp()

    def test_yatra_login(self):
        utility = SeleniumUtilities()
        driver = utility.launch_browser(Yatra.yatra_url)
        login_title = utility.get_title(driver, YatraXpath.login)
        print("TITLE", login_title)
        utility.send_keys(driver, YatraXpath.login,"test2@gmail.com", 'css')

        def tearDown(self):
            print("all tests done")
            pass
