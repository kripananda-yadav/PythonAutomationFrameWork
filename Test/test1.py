from selenium import webdriver
import sys
import unittest
class HomePageTest(unittest.TestCase):

#Setting up the Path for the Refrence
path = r'C:\HCM\PythonAutomationFrameWork'
sys.path.insert(0,path)

#Refrence of the Reuseable Class
from common.executeBrowser import start_page
from PageObjects.HomePageObject import homePageObject
from common.selector import selector


#Driver Initialization
driver = webdriver.Chrome(executable_path=r'C:\HCM\PythonAutomationFrameWork\webdriver\chromedriver.exe')

    @classmethod
    def SetUpClass(cls):
        #Object Creation
        cls.start_obj = start_page(driver)
        cls.homepage_object = homePageObject()
        cls.select = selector(driver)
        cls.start_obj.maximze()

    
    def test_login(self):
        self.start_obj.navigate(self.homepage_object.Url)
        self.select.input_text("Xpath",self.homepage_object.emailXpath,self.homepage_object.userEmail)
        self.select.input_text("XPath",self.homepage_object.passwordXpath,self.homepage_object.userPassword)
        self.select.click("XPath",self.homepage_object.loginButtonXpath)
        self.driver.implicitly_wait(100)


    @classmethod
    def tearDownClass(self):
        self.driver.clos()
        self.driver.quit()
        print("Test has been completed")
    
