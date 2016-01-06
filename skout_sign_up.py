'''
Created on Jul 30, 2015

@author: Sailee29
'''
import os
import unittest
from appium import webdriver
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
         
        """ Search for sign up button """    
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/prelogin_signup")))
        element.click()
        
        """Enter all the details""" 
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "Name")))
        element.send_keys("tester04")
        self.driver.find_element_by_id("com.skout.android:id/signup_gender_female").click()
        
        self.driver.find_element_by_id("com.skout.android:id/signup_birthday").click()
        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='0']").send_keys("Jun") 
        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='1']").send_keys('18')
        self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='2']").send_keys('1992')
        self.driver.find_element_by_id("android:id/button1").click()
        
        self.driver.find_element_by_id("com.skout.android:id/signup_interest_both").click()
        
        """ Insert profile picture """
        self.driver.find_element_by_id("com.skout.android:id/signup_profile_icon").click()
        self.driver.find_element_by_name("Documents").click()
        self.driver.find_element_by_name("Recent").click()
        self.driver.find_element_by_name("Aug 14").click()
        self.driver.find_element_by_id("com.skout.android:id/crop_image_ok").click()    
         
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
         
        """ Enter email address and password """
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/emailField")))
        element.send_keys("abcdef@9.com")
        self.driver.find_element_by_id("com.skout.android:id/pwField").send_keys("password")
        self.driver.find_element_by_id("com.skout.android:id/confirmPwField").send_keys("password")
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
        
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "Skip")))
        element.click()
        
        """ Handle captcha """
        """sleep(20)
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.CheckBox")').click()
        sleep(20)
        el = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
        print el 
        el[3].click()
        sleep(4)
        self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
        """
        
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SkoutAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)