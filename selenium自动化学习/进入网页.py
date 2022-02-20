# coding = utf-8
from selenium import webdriver
import time


browser = webdriver.Chrome()
first_url = "http://www.baidu.com"
browser.get(first_url)
time.sleep(1)
second_url = 'http://news.baidu.com'
browser.get(second_url)
time.sleep(2)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
# print(browser.title)
# print(browser)
time.sleep(0.5)
browser.maximize_window()  # 窗口最大化
time.sleep(0.5)
# browser.set_window_size(480, 800)  # 设置窗口大小
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()