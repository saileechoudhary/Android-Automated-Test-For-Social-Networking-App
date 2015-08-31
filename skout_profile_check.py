'''
Created on Aug 7, 2015

@author: Sailee29
'''
import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from appium.webdriver.webelement import WebElement
import random
from selenium.common.exceptions import NoSuchElementException
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
 
        
 
 
 
#     def tearDown(self):
#         "Tear down the test"
#         self.driver.quit()
 
    def test_profile_check(self):
                     
#         "Test if sign up works correctly"
#         "Sign up the user" 
#         sleep(7)        
#         element = self.driver.find_element_by_id("com.skout.android:id/prelogin_signup")
#         element.click()
#                  
#         self.driver.find_element_by_name("Name").send_keys("Tester3")
#         self.driver.find_element_by_id("com.skout.android:id/signup_gender_female").click()
#         
#         self.driver.find_element_by_id("com.skout.android:id/signup_birthday").click()
#         self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='0']").send_keys('Jan') 
#         self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='1']").send_keys('20')
#         self.driver.find_element_by_xpath("//android.widget.NumberPicker[@index='2']").send_keys('1995')
#         self.driver.find_element_by_id("android:id/button1").click()
#         
#         self.driver.find_element_by_id("com.skout.android:id/signup_interest_male").click()
#         
#         self.driver.find_element_by_id("com.skout.android:id/signup_profile_icon").click()
#         self.driver.find_element_by_name("Documents").click()
#         self.driver.find_element_by_id("android:id/up").click()
#         self.driver.find_element_by_name("Recent").click()
#         self.driver.find_element_by_name("Aug 3").click()
#         self.driver.find_element_by_id("com.skout.android:id/crop_image_ok").click()    
#         
#         self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
#         
#         self.driver.find_element_by_id("com.skout.android:id/emailField").send_keys("tester3@b.com")
#         self.driver.find_element_by_id("com.skout.android:id/pwField").send_keys("password")
#         self.driver.find_element_by_id("com.skout.android:id/confirmPwField").send_keys("password")
#         self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
#         sleep(40)
#         print self.driver.contexts
#         print self.driver.current_context
#         #self.driver.switch_to.context("WEBVIEW_com.skout.android")
#         print self.driver.current_context
#         
#         self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.CheckBox")').click()
#         sleep(20)
#         el = self.driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.Button")')
#         print el 
#         el[3].click()
#         
#         #submit button
#         self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.Button")').click()
#         
#         self.driver.find_element_by_id("com.skout.android:id/menu_skip").click()
        "Login with profile"
        sleep(25)
        element = self.driver.find_element_by_id("com.skout.android:id/prelogin_login_here")
        element.click()
        
        self.driver.find_element_by_id("com.skout.android:id/emailField").send_keys("test@abc.com")
        self.driver.find_element_by_id("com.skout.android:id/pwField").send_keys("password")
        self.driver.find_element_by_id("com.skout.android:id/doneBtn").click()
        sleep(30)
        
        try:
            self.driver.find_element_by_name("Done")
        except NoSuchElementException:
            ""
            
        "Check 10 profiles randomly"
        self.driver.find_element_by_name("Tap to edit search settings").click()
        
        self.driver.find_element_by_id("com.skout.android:id/show_me_row_label").click()
        self.driver.find_element_by_name("Men who like women").click()
        
        
             
        sleep(5)
        #age_min = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.skout.android:id/search_content_layout']")
#         print age_min.get_attribute("resource-id")
        age_min = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.skout.android:id/search_age']/android.widget.RelativeLayout[1]/android.widget.AdapterView/android.widget.FrameLayout/android.widget.TextView[@text=19]")
        #print age_min.get_attribute("text")
        
        age_min.click()
        #age_min.click()
        #age[0].send_keys("18")
        #age[1].send_keys("21")
        #self.driver.scroll(18, 21)
        el = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.skout.android:id/search_age']/android.widget.RelativeLayout[1]/android.widget.AdapterView/android.widget.FrameLayout/android.widget.TextView[@text=18]")
#         action = TouchAction(self.driver)
#         action.press(age_min).move_to(el).release().perform()
#         
#         self.driver.drag_and_drop(el, age_min)
        
        
        looping = True
        while looping:
            try:
                sleep(7)
                #print "inside try"
                age_max = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.skout.android:id/search_age']/android.widget.RelativeLayout[@resource-id='com.skout.android:id/search_age_max']/android.widget.AdapterView/android.widget.FrameLayout/android.widget.TextView[@text=19]")
                #print age_max.get_attribute("text")
                looping = False
            except NoSuchElementException:
                self.driver.swipe(186, 898, 680, 898, 800)
        
        
        self.driver.find_element_by_id("com.skout.android:id/menu_done").click()
        sleep(10)
        #names = self.driver.find_element_by_android_uiautomator(
        ##'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceId("com.skout.android:id/explore_button_name").instance(0));')
       
        
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
                
                self.driver.find_element_by_id("com.skout.android:id/profile_tabs_info_tab").click()
                #gender = self.driver.find_element_by_id('com.skout.android:id/profile_info_gender')
            
                #el1 = self.driver.find_element_by_id("com.skout.android:id/profile_tabs_info_tab")
                self.driver.swipe(497, 780, 497, 480, 500)
            #self.driver.execute_script("mobile: scrollTo",{"element": self.el1.id})
            #gender = self.driver.find_element_by_android_uiautomator('new UiSelector().scrollable(true).resourceId("com.skout.android:id/profile_info_gender")')
            #gender = self.driver.scrollTo(self.driver.find_element_by_id('com.skout.android:id/profile_info_gender'))
                gender = self.driver.find_element_by_id('com.skout.android:id/profile_info_gender')
            
                            
                if gender.get_attribute("text") == "Male":
                    print gender.get_attribute("text")
                else:
                    print "Error - Not a Male"
            
                age = self.driver.find_element_by_id("com.skout.android:id/profile_info_age")
                #print age.get_attribute("text")
                temp = age.get_attribute("text")
#                 print temp
                
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
                       
        self.driver.swipe(497, 600, 497, 480, 500)
        
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
        
        #print "Random items"
        #print rand_item, rand_item1
              
        
        
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SkoutAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)