from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

ser = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://rollercoin.com/game")

time.sleep(8)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "geetest_radar_tip"))
    )
    pyautogui.moveTo(650, 947, 1)
    pyautogui.moveTo(700, 950, 0.5)
    pyautogui.moveTo(675, 935, 0.5)
    element.click()
except:
    driver.quit()

email = driver.find_element(By.NAME, 'mail')
email.send_keys('EMAIL_HERE')

time.sleep(2)

password = driver.find_element(By.NAME, 'password')
password.send_keys('PASSWORD_HERE')

time.sleep(1)
pyautogui.scroll(-50)

time.sleep(1)
pyautogui.moveTo(669, 980, 1)
log_in_button = driver.find_element(By.XPATH, '//div[@class="form-group mt-4"]//button[@class="btn btn-default-btn w-100"]')
log_in_button.click()

time.sleep(5)

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='electricity-recharge-btn-container']//button[@class='tree-dimensional-button btn-cyan electricity-recharge-btn ']")))
    pyautogui.moveTo(288, 498, 2.5)
    element.click()
    time.sleep(2)
    driver.quit
except:
    print("Unable to locate element.")
