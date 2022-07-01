#ROLLERCOIN BOT
# Importing Modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# Initializing "ser" variable and assigning it the Service class with the argument being the path to the chromedriver file.
ser = Service("C:\Program Files (x86)\chromedriver.exe")

# Initializing "driver" variable and assigning it webdriver.Chrome with the service argument being equal to ser.
driver = webdriver.Chrome(service=ser)

# This opens the Chrome browser and goes to the website assigned for it to go.
driver.get("https://rollercoin.com/game")

# Stops script from running for 8 secs.
time.sleep(8)

# Pauses script till it locates the precense of the verify button/specified element.
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "geetest_radar_tip"))
    )
    
    # Using pyautogui to simulate mouse movement on the verify button.
    pyautogui.moveTo(650, 947, 1)
    pyautogui.moveTo(700, 950, 0.5)
    pyautogui.moveTo(675, 935, 0.5)
    
    # Clicks specified element
    element.click()

# If the code above is not executable, driver will close the browser.
except:
    driver.quit()

# Finds the element where email should be input and sends keys (email) to it.
email = driver.find_element(By.NAME, 'mail')
email.send_keys('EMAIL_HERE')

# Sleeps script for 2 secs
time.sleep(2)

#  Finds the element where password should be input and sends keys (password) to it.
password = driver.find_element(By.NAME, 'password')
password.send_keys('PASSWORD_HERE')

# Sleeps script for one seconds and scrolls to make log in button visible
time.sleep(1)
pyautogui.scroll(-50)

# Sleeps for 1 sec
time.sleep(1)

# Simulates mouse movement to log in button and clicks the button
pyautogui.moveTo(669, 980, 1)
log_in_button = driver.find_element(By.XPATH, '//div[@class="form-group mt-4"]//button[@class="btn btn-default-btn w-100"]')
log_in_button.click()

# Sleeps script for 5 secs
time.sleep(5)

# Pauses script until presence of recharge button/specified element is located
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='electricity-recharge-btn-container']//button[@class='tree-dimensional-button btn-cyan electricity-recharge-btn ']")))
   
    # Simulates mouse movement to recharge button and clicks it
    pyautogui.moveTo(288, 498, 2.5)
    element.click()
    
    # Sleeps driver to let recharge render in and closes the browser.
    time.sleep(2)
    driver.quit()
    
# Won't execute unless the above code is not executable. This just lets me know the code wasn't able to locate the specified element. 
except:
    print("Unable to locate element.")
