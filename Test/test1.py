from selenium import webdriver
import sys
#

path = r'C:\Users\kripanandayadav\python'
sys.path.insert(0,path)
# print(sys.path)

from common.executeBrowser import start_page
from common.selector import selector
# from common.executeBrowser import *
# from common.selector import *
# from ServicePage.HomePageObject import *


driver = webdriver.Chrome(executable_path=r'C:\Users\kripanandayadav\python\webdriver\chromedriver.exe')

start_obj = start_page(driver,"https://demoqa.com/text-box")
start_obj.maximze()
start_obj.navigate()
    
select_obj = selector(driver,"XPATH","//input[@type='text']")
click_obj = selector(driver,"XPATH","//*[@id='Katalon']")
select_obj.input_text("Siaskd")
click_obj.clickable()