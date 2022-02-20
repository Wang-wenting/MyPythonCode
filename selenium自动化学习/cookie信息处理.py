#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")# 获得cookie信息
cookie= driver.get_cookies()#将获得cookie的信息打印
for c in cookie:
    print(c)

driver.quit()