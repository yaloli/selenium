from selenium import webdriver
import chromedriver_autoinstaller

class chrome_driver:
    def __init__(self):
        self.path = chromedriver_autoinstaller.install()
    
    def getDriver(self):
        return webdriver.Chrome(self.path)

