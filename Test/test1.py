from selenium import webdriver
import sys

#Setting up the Path for the Refrence
path = r'C:\HCM\PythonAutomationFrameWork'
sys.path.insert(0,path)

#Refrence of the Reuseable Class
from common.executeBrowser import start_page
from PageObjects.HomePageObject import homePageObject
from common.selector import selector

#Driver Initialization
driver = webdriver.Chrome(executable_path=r'C:\HCM\PythonAutomationFrameWork\webdriver\chromedriver.exe')

#Object Creation
start_obj = start_page(driver)
homepage_object = homePageObject()
select = selector(driver)


start_obj.maximze()
start_obj.navigate(homepage_object.Url)

select.input_text("Xpath",homepage_object.emailXpath,homepage_object.userEmail)
select.input_text("XPath",homepage_object.passwordXpath,homepage_object.userPassword)
select.click("XPath",homepage_object.loginButtonXpath)
driver.implicitly_wait(100)
    
