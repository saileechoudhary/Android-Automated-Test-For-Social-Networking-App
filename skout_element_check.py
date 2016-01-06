'''
Created on Jul 30, 2015

@author: Sailee29
'''
import os
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 
 
class SkoutAndroidTests(unittest.TestCase):
    "Class to run tests against the Skout app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'emulator-5554'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'C:/Users/Sailee29/Downloads/skout.apk'))
        desired_caps['appPackage'] = 'com.skout.android'
        desired_caps['appActivity'] = 'com.skout.android.activities.Skout'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_all_elements(self):
               
        
        "Test if all elements are present"
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/prelogin_login_here")))
        element.click()
                
        """Login using credentials"""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/emailField")))
        element.send_keys("blue143")
        #self.driver.find_element_by_id("com.skout.android:id/emailField").send_keys("blue143")
        self.driver.find_element_by_id("com.skout.android:id/pwField").send_keys("21143")
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
        
        
        try:
            self.driver.find_element_by_name("Done").click()
        except NoSuchElementException:
            ""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "Meet People")))
        element.click()
        
        
        "Check if all elements are present"
        try:
            self.driver.find_element_by_name("Meet People")
            print "'Meet people' is present"    
        except NoSuchElementException:
            print "'Meet people' is not present"
            
        try:    
            self.driver.find_element_by_name("Buzz")
            print "'Buzz' is present"
        except NoSuchElementException:
            print "'Buzz' is not present"
        
        try:
            self.driver.find_element_by_name("Chats")
            print "'Chats' is present"
        except NoSuchElementException:
            print "'Chats' is not present"
            
        try:    
            self.driver.find_element_by_name("Shake To Chat")
            print "'Shake to chat' is present"
        except NoSuchElementException:
            print "'Shake to chat' is not present"
        
        try:
            self.driver.find_element_by_name("Go Premium")
            print "Go Premium available"
        except NoSuchElementException:
            print "Go Premium not available"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Who Checked Me Out?").instance(0));')
            print "'Who Checked Me Out' is present"
        except NoSuchElementException:
            print "'Who Checked Me Out' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Who Favorited Me?").instance(0));')
            print "'Who Favorited Me?' is present"
        except NoSuchElementException:
            print "'Who Favorited Me?' is not present"
        
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Skout Travel").instance(0));')
            print "'Skout Travel' is present"
        except NoSuchElementException:
            print "'Skout Travel' is not present"
            
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Get Points").instance(0));')
            print "'Get Points' is present"
        except NoSuchElementException:
            print "'Get Points' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Send Wink Bomb!").instance(0));')
            print "'Send Wink Bomb!' is present"
        except NoSuchElementException:
            print "'Send Wink Bomb!' is not present"  
            
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Feature Me!").instance(0));')
            print "'Feature Me!' is present"
        except NoSuchElementException:
            print "'Feature Me!' is not present" 
            
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Contacts").instance(0));')
            print "'Contacts' is present"
        except NoSuchElementException:
            print "'Contacts' is not present"    
            
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Add Friends").instance(0));')
            print "'Add Friends' is present"
        except NoSuchElementException:
            print "'Add Friends' is not present"     
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Add Friends").instance(0));')
            print "'Add Friends' is present"
        except NoSuchElementException:
            print "'Add Friends' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Find User by SkoutID").instance(0));')
            print "'Find User by SkoutID' is present"
        except NoSuchElementException:
            print "'Find User by SkoutID' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Settings").instance(0));')
            print "'Settings' is present"
        except NoSuchElementException:
            print "'Settings' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Skout Blog").instance(0));')
            print "'Skout Blog' is present"
        except NoSuchElementException:
            print "'Skout Blog' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Get Skout+").instance(0));')
            print "'Get Skout+' is present"
        except NoSuchElementException:
            print "'Get Skout+' is not present"
            
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Skout Safety").instance(0));')
            print "'Skout Safety' is present"
        except NoSuchElementException:
            print "'Skout Safety' is not present"
            
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Terms of Use").instance(0));')
            print "'Terms of Use' is present"
        except NoSuchElementException:
            print "'Terms of Use' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Privacy Policy").instance(0));')
            print "'Privacy Policy' is present"
        except NoSuchElementException:
            print "'Privacy Policy' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Rate Us!").instance(0));')
            print "'Rate Us!' is present"
        except NoSuchElementException:
            print "'Rate Us!' is not present"
        
        try:    
            self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Logout").instance(0));')
            print "'Logout' is present"
        except NoSuchElementException:
            print "'Logout' is not present"    
                
       
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SkoutAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)