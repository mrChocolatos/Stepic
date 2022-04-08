import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )
y = browser.find_element_by_id('book')
y.click()

w = browser.find_element_by_id('input_value').text
    # WebDriverWait(browser, 13).until(EC.invisibility_of_element((By.XPATH, '//*[@id="input_value"]')))

yer = calc(w)
yte = browser.find_element_by_id('answer')
yte.send_keys(yer)
yer = browser.find_element_by_id('solve')
yer.click()
