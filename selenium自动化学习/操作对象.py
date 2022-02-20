#coding=utf-8
from selenium import webdriver
import  time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(30)
#id = cp 元素的文本信息
data = driver.find_element_by_id("bottom_layer").text
print(data)  #打印信息'

driver.quit()