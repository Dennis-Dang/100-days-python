from selenium import webdriver
from dotenv import dotenv_values
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

config = dotenv_values('.env')
chrome_driver_path = config["CHROME_DRIVER_PATH"]

# Prevents chrome driver from automatically closing after starting.
options = ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(chrome_driver_path),
    options=options
)
item_upgrades = [
    "Cursor",
    "Grandma",
    "Factory",
    "Mine",
    "Shipment",
    "Alchemy lab",
    "Portal",
    "Time machine",
    "Elder Pledge"
]
available_items = [None] * len(item_upgrades)


def get_money() -> int:
    money_elem = driver.find_element(By.ID, 'money')
    return int(money_elem.text)


def get_most_expensive():
    for i in range(len(item_upgrades)):
        available_items[i] = driver.find_element(By.ID, 'buy' + item_upgrades[i])

    found_item = None
    for item in reversed(available_items):
        if found_item is None and item.get_attribute("class") == "":
            found_item = item

    if found_item is not None:
        found_item.click()


driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')
timeout = time.time() + 5
# 5 minutes from now
five_min = time.time() + 60*5

loop = True
while loop:
    cookie.click()
    # For every 5 seconds:
    if time.time() > timeout:
        pass
        # Check if upgrades available and purchase them.
    elif time.time() == five_min:
        loop = False
        # Print Cookies/Sec after 5 Minutes have passed.
        print(driver.find_element(By.ID, "cps").text)


