#coding=utf-8
from selenium import webdriver
import time
#访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=500"
driver.execute_script(js)
time.sleep(3)#将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

driver.quit()