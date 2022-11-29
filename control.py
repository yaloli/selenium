import time
from MySel import chrome_driver

urls = ["https://www.naver.com", "https://www.google.co.kr", "https://www.youtube.com"]
url = urls[0]

driver = chrome_driver().getDriver()
driver.get(url)