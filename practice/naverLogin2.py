import time
import chromedriver_autoinstaller
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.by import By

def clipboard_input(selector, user_input):
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

    pyperclip.copy(user_input)
    driver.find_element(By.CSS_SELECTOR, selector).click()
    # # 윈도우
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    # 맥
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    # # 다른방법
    # pyautogui.keyDown('command')
    # pyautogui.press('v')
    # pyautogui.keyUp('command')
    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴 
    time.sleep(1)

url = "https://www.naver.com"
login = {
    "id": "id",
    "pw": "pw"
}
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)
driver.implicitly_wait(5)

driver.get(url)
login_page = driver.find_element(By.CSS_SELECTOR, "#account > a").get_attribute("href")
driver.get(login_page)
clipboard_input("#id", login["id"])
clipboard_input("#pw", login["pw"])
driver.find_element(By.ID, "log.login").click()

time.sleep(2)

