import os
import unittest
import time
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = '9781ca80'
        #desired_caps['app'] = PATH(
        #    '../../../sample-code/apps/ContactManager/ContactManager.apk'
        #)
        desired_caps['appPackage'] = 'com.huawei.ioc'
        desired_caps['appActivity'] = '.ui.activities.LoginActivity'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['unicodeKeyboard'] ='True'
        desired_caps['resetKeyboard'] ='True'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        time.sleep(3)


        textfields_1 = self.driver.find_element_by_id("com.huawei.ioc:id/et_input_user_name")
        textfields_1.send_keys("test1")
        textfields_2 = self.driver.find_element_by_id("com.huawei.ioc:id/et_password")
        textfields_2.send_keys("Pr0d1234")

        self.assertEqual('test1', textfields_1.text)

        el = self.driver.find_element_by_id('com.huawei.ioc:id/btn_login')
        el.click()






if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)