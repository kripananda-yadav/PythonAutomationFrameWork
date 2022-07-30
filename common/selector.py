from selenium.webdriver.common.by import By

class selector:
    def __init__(self,driver,selectorType,identifier):
        self.driver = driver
        self.selectorType = selectorType
        self.identifier = identifier

    def input_text(self,keys):
        if self.selectorType == "CLASS_NAME":
            self.driver.find_element(By.CLASS_NAME,self.identifier).send_keys(keys)

        elif self.selectorType == "CSS_SELECTOR":
            self.driver.find_element(By.CSS_SELECTOR,self.identifier).send_keys(keys)

        elif self.selectorType == "ID":
            self.driver.find_element(By.ID,self.identifier).send_keys(keys)

        elif self.selectorType == "LINK_TEXT":
            self.driver.find_element(By.LINK_TEXT,self.identifier).send_keys(keys)

        elif self.selectorType == "NAME":
            self.driver.find_element(By.NAME,self.identifier).send_keys(keys)

        elif self.selectorType == "PARTIAL_LINK_TEXT":
            self.driver.find_element(By.PARTIAL_LINK_TEXT ,self.identifier).send_keys(keys)

        elif self.selectorType == "TAG_NAME":
            self.driver.find_element(By.TAG_NAME,self.identifier).send_keys(keys)

        elif self.selectorType == "XPATH":
            self.driver.find_element(By.XPATH,self.identifier).send_keys(keys)

    def clickable(self):
        if self.selectorType == "CLASS_NAME":
            self.driver.find_element(By.CLASS_NAME,self.identifier).click()

        elif self.selectorType == "CSS_SELECTOR":
            self.driver.find_element(By.CSS_SELECTOR,self.identifier).click()

        elif self.selectorType == "ID":
            self.driver.find_element(By.ID,self.identifier).click()

        elif self.selectorType == "LINK_TEXT":
            self.driver.find_element(By.LINK_TEXT,self.identifier).click()

        elif self.selectorType == "NAME":
            self.driver.find_element(By.NAME,self.identifier).click()

        elif self.selectorType == "PARTIAL_LINK_TEXT":
            self.driver.find_element(By.PARTIAL_LINK_TEXT ,self.identifier).click()

        elif self.selectorType == "TAG_NAME":
            self.driver.find_element(By.TAG_NAME,self.identifier).click()

        elif self.selectorType == "XPATH":
            self.driver.find_element(By.XPATH,self.identifier).click()
