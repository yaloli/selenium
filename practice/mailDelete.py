import time
import naverLogin2
from selenium.webdriver.common.by import By

url = "https://mail.naver.com/"
driver = naverLogin2.driver
driver.get(url)
time.sleep(5)

while True:
    driver.execute_script("document.querySelector('[for=\"selection_all\"]').click()")
    driver.execute_script("document.querySelector('button.button_task.svg_delete').click()")
    time.sleep(0.5)
    if len(driver.find_elements(By.CSS_SELECTOR, ".page_list>li"))<=4:
        break
