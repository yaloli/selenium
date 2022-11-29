import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.naver.com"
login = {
    "id": "id",
    "pw": "pw"
}
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)

driver.get(url)

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "#account > a").click()
driver.find_element(By.ID, "id").send_keys(login['id'])
time.sleep(1)
driver.find_element(By.ID, "pw").send_keys(login['pw'])
time.sleep(1)

driver.find_element(By.ID, "log.login").click()
