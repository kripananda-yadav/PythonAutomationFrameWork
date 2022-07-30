class start_page:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def navigate(self):
        self.driver.get(self.url)

    def maximze(self):
        self.driver.maximize_window()

