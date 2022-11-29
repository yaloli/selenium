import time
import chromedriver_autoinstaller 
from selenium import webdriver

url = "https://www.naver.com"
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

driver.get(url)