import math
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id('treasure')
x = x_element.get_attribute('valuex')
y = calc(x)
inpuT_elem = browser.find_element_by_xpath('//*[@id="answer"]')
inpuT_elem.send_keys(f'{y}')
button_1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
button_1.click()
button_2 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
button_2.click()
button_3 = browser.find_element_by_xpath('/html/body/div/form/button')
button_3.click()

time.sleep(15)
