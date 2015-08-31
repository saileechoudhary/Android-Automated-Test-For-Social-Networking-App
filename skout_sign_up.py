'''
Created on Jul 30, 2015

@author: Sailee29
'''
import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
class SkoutAndroidTests(unittest.TestCase):
    "Class to run tests against the Skout app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'emulator-5554'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'C:/Users/Sailee29/Downloads/skout.apk'))
        desired_caps['appPackage'] = 'com.skout.android'
        desired_caps['appActivity'] = 'com.skout.android.activities.Skout'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_sign_up(self):
               
         
        "Test if sign up works correctly"
        sleep(7)        
        element = self.driver.find_element_by_id("com.skout.android:id/prelogin_signup")
        element.click()
        
         
        self.driver.find_element_by_name("Name").send_keys("tester04")
        self.driver.find_element_by_id("com.skout.android:id/signup_gender_female").click()
        
        self.driver.find_element_by_id("com.skout.android:id/signup_birthday").click()
        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='0']").send_keys("Jun") 
        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='1']").send_keys('18')
        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='2']").send_keys('1992')
        self.driver.find_element_by_id("android:id/button1").click()
        
        self.driver.find_element_by_id("com.skout.android:id/signup_interest_both").click()
        
        #self.driver.find_element_by_id("com.skout.android:id/signup_profile_icon").click()
#         #self.driver.find_element_by_xpath("//android.widget.ListView[@index='0']").send_keys('Jun') 
#         self.driver.find_element_by_name("Documents").click()
#         #temp.find_element_by_class_name("android.widget.LinearLayout[@index='0']").click()
#         #self.driver.find_element_by_id("android:id/up").click()
#         self.driver.find_element_by_name("Recent").click()
#         #self.driver.find_element_by_id("com.android.documentsui:id/grid")
#         self.driver.find_element_by_name("Aug 14").click()
#         #textfields = self.driver.find_element_by_id("android:id/action_bar_title")
#         #self.assertEqual('Select thumbnail image', textfields)
#         self.driver.find_element_by_id("com.skout.android:id/crop_image_ok").click()    
#         
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
#         #textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
#         #self.assertEqual('MATCH SETTINGS', textfields[0].text)
#         print "test"
        
        self.driver.find_element_by_id("com.skout.android:id/emailField").send_keys("abcdef@9.com")
        self.driver.find_element_by_id("com.skout.android:id/pwField").send_keys("password")
        #self.driver.find_element_by_xpath("android.widget.EditText[@NAF='true']").send_keys("password")
        self.driver.find_element_by_id("com.skout.android:id/confirmPwField").send_keys("password")
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
        
        sleep(20)
        print self.driver.contexts
        print self.driver.current_context
        #self.driver.switch_to.context("WEBVIEW_com.skout.android")
        print self.driver.current_context
        
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.CheckBox")').click()
        sleep(20)
        el = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
        print el 
        el[3].click()
        sleep(4)
        #submit button
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
        #self.driver.find_element_by_id("com.skout.android:id/menu_skip").click()
        
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SkoutAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)