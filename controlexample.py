import pyperclip
import time
from MySel import chrome_driver
import platform
import Naver as TARGET_PAGE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def clipboard_input(selector, user_input, driver):
    temp_user_input = pyperclip.paste() 
    operating_system = {
        'Darwin':ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform,
        'Windows':ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform
    }
    pyperclip.copy(user_input)
    driver.find_element(By.CSS_SELECTOR, selector).click()
    operating_system[platform.system()]()
    pyperclip.copy(temp_user_input) 
    time.sleep(1)

def login(driver):
    url = TARGET_PAGE.LOGIN_PAGE
    login = {
        "id": TARGET_PAGE.ID,
        "pw": TARGET_PAGE.PW
    }
    driver.get(url)
    clipboard_input(TARGET_PAGE.ID_INPUT, login["id"], driver)
    clipboard_input(TARGET_PAGE.PW_INPUT, login["pw"], driver)
    driver.find_element(By.ID, TARGET_PAGE.LOGIN_BUTTON).click()

def to_mail(driver):
    url = TARGET_PAGE.MAIL_PAGE
    driver.get(url)
    time.sleep(3)

def delete_mail(driver):
    while len(driver.find_elements(By.CSS_SELECTOR, ".page_list>li"))>4:
        driver.execute_script("document.querySelector('[for=\"selection_all\"]').click()")
        driver.execute_script("document.querySelector('button.button_task.svg_delete').click()")
        time.sleep(0.5)

def main():
    driver = chrome_driver().getDriver()
    login(driver)
    to_mail(driver)
    delete_mail(driver)

if __name__=="__main__":
    main()