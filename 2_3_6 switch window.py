# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]

import math
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)

button_1 = browser.find_element_by_xpath('/html/body/form/div/div/button')
button_1.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
inpuT_elem = browser.find_element_by_xpath('//*[@id="answer"]')
inpuT_elem.send_keys(f'{y}')
button_2 = browser.find_element_by_xpath('/html/body/form/div/div/button')
button_2.click()

time.sleep(15)

browser.quit()
