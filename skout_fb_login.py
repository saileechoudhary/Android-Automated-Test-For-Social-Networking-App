'''
Created on Aug 9, 2015

@author: Sailee29
'''
import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
 
class SkoutAndroidTests(unittest.TestCase):
    "Class to run tests against the Skout app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'C:/Users/Sailee29/Downloads/skout.apk'))
        desired_caps['appPackage'] = 'com.skout.android'
        desired_caps['appActivity'] = 'com.skout.android.activities.Skout'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_fb_login(self):
               
        "Test if login with Facebook works correctly"
        sleep(5)
        element = self.driver.find_element_by_id("com.skout.android:id/prelogin_fb_button")
        element.click()
                 
        #self.driver.switch_to.context("WEBVIEW_com.skout.android")
        
        sleep(7)
        logon_elems = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.EditText")')
        print logon_elems
        logon_elems[0].send_keys("sailee.choudhary@gmail.com")
        logon_elems[1].send_keys("fblogin1@")
        sleep(10)
        login_button = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
        print login_button
        login_button[0].click()
        
        sleep(5)
        ok_button = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
        print ok_button
        ok_button[1].click()
        #self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
        
        #self.driver.find_element_by_android_uiautomator('new UiSelector().description("Welcome to Facebook")')
        #self.driver.find_element_by_class_name("android.widget.EditText")
        #temp = self.driver.find_element_by_xpath("//android.webkit.WebView/android.view.View[@index='0']")
        #print temp
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SkoutAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)