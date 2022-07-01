#ROLLERCOIN BOT - Improved version
# Importing modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# Selenium boilerplate 
ser = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://rollercoin.com/game")
