#-*-coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(2)

m=driver.find_element_by_id("s-user-setting-menu")
# m = driver.find_element_by_class_name("s-user-setting-pfmenu")
print(m.text)
driver.find_element_by_class_name("setpref").click()

time.sleep(3)

driver.quit()