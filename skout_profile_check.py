'''
Created on Aug 7, 2015

@author: Sailee29
'''
import os
import unittest
from appium import webdriver
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
 
class SkoutAndroidTests(unittest.TestCase):
    "Class to run tests against the Skout app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'C:/Users/Sailee29/Downloads/skout.apk'))
        desired_caps['appPackage'] = 'com.skout.android'
        desired_caps['appActivity'] = 'com.skout.android.activities.Skout'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_profile_check(self):
                     
        """Login with profile"""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/prelogin_login_here")))
        element.click()
        
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/emailField")))
        element.send_keys("test@abc.com")
        self.driver.find_element_by_id("com.skout.android:id/pwField").send_keys("password")
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
        sleep(30)
        
        try:
            self.driver.find_element_by_name("Done").click()
        except NoSuchElementException:
            ""
            
        "Check 10 profiles randomly"
        self.driver.find_element_by_name("Tap to edit search settings").click()
        
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.skout.android:id/show_me_row_label")))
        element.click()
        self.driver.find_element_by_name("Men who like women").click()
         
         
        age_min = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.LinearLayout[@resource-id='com.skout.android:id/search_age']/android.widget.RelativeLayout[1]/android.widget.AdapterView/android.widget.FrameLayout/android.widget.TextView[@text=19]")))
        age_min.click()                   
        
        #age_min.click()
        #age[0].send_keys("18")
        #age[1].send_keys("21")
        #self.driver.scroll(18, 21)
             
        looping = True
        while looping:
            try:       
                age_max = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.LinearLayout[@resource-id='com.skout.android:id/search_age']/android.widget.RelativeLayout[@resource-id='com.skout.android:id/search_age_max']/android.widget.AdapterView/android.widget.FrameLayout/android.widget.TextView[@text=19]")))
                #print age_max.get_attribute("text")
                looping = False
            except NoSuchElementException:
                #self.driver.swipe(186, 898, 680, 898, 800)
                ""
        
        self.driver.find_element_by_id("com.skout.android:id/menu_done").click()
        
       
        """ function to check each profile"""
        def random_items(itemlist):
            for item in itemlist:
                print item.get_attribute("text")
                item.click()
                try:
                    self.driver.find_element_by_name("Done").click()
                #self.driver.find_elements_by_name("No, Thanks").click()
                except NoSuchElementException:
                    print  ""
                
                self.driver.swipe(497, 680, 497, 480, 500)
                
                element = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.NAME, "INFO")))
                element.click()
                self.driver.swipe(497, 780, 497, 480, 500)
                gender = self.driver.find_element_by_id('com.skout.android:id/profile_info_gender')
            
                            
                if gender.get_attribute("text") == "Male":
                    print gender.get_attribute("text")
                else:
                    print "Error - Not a Male"
            
                age = self.driver.find_element_by_id("com.skout.android:id/profile_info_age")
                #print age.get_attribute("text")
                temp = age.get_attribute("text")
#                                 
                if temp > 21:
                        #print "checking age"
                        print age.get_attribute("text")
                else:
                    print "Age not in range"
                
                interested = self.driver.find_element_by_android_uiautomator(
        'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("com.skout.android:id/profile_info_interested_in").instance(0));')
                
                if interested.get_attribute("text") == "Women":
                    print "Interested in %s" %(interested.get_attribute("text"))
                else:
                    print "Error - Interested in Men & Women"
                
                self.driver.find_element_by_id("android:id/up").click()     
        
       
        #self.driver.swipe(470, 420, 470,180, 400)
        
        """ Randomly select 10 profiles and pass them to the function """
        names = self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.skout.android:id/explore_button_name")')
        print names
        rand_item = random.sample(names, 5)
        print rand_item
        
        random_items(rand_item)
        sleep(7)
        
        self.driver.swipe(497, 980, 497, 480, 500)
        names1 = self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.skout.android:id/explore_button_name")')
        print names1
        rand_item1 = random.sample(names1, 5)
        
        random_items(rand_item1)
        
       
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SkoutAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)